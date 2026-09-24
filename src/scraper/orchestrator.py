"""Main scraper orchestrator that ties all modules together."""

from __future__ import annotations

import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Callable

from src.core.config import MAX_WORKERS, get_docs_dir, get_page_url_template
from src.core.updater import UpdateChecker
from src.scraper.catalog import CatalogNode, get_catalog_tree, flatten_catalog
from src.scraper.content import fetch_content_html
from src.scraper.converter import get_safe_filename, html_to_markdown


ProgressCallback = Callable[[int, int, str], None]
"""Callback signature: (current, total, message)."""


def _get_output_dir(node: CatalogNode) -> Path:
    """Determine the output directory for a page based on its category path."""
    docs_dir = get_docs_dir()
    # category_path uses "/" separators
    parts = node.category_path.split("/") if node.category_path else []
    # Sanitize each part for use as a directory name
    safe_parts = [p for p in parts if p]
    if not safe_parts:
        safe_parts = ["未分类"]
    return docs_dir.joinpath(*safe_parts)


def _write_markdown(
    node: CatalogNode, markdown: str, output_dir: Path
) -> Path:
    """Write the markdown content to a file, with YAML front matter."""
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = get_safe_filename(node.title)
    filepath = output_dir / filename

    page_url = get_page_url_template().format(path_id=node.path_id)
    front_matter = (
        "---\n"
        f"title: {node.title}\n"
        f"path_id: {node.path_id}\n"
        f"updated_at: {node.updated_at}\n"
        f"category: {node.category_path}\n"
        f"source_url: {page_url}\n"
        "---\n\n"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write(markdown)

    return filepath


def scrape_page(node: CatalogNode) -> Path:
    """Scrape a single page and save it as markdown.

    Args:
        node: The catalog node for the page.

    Returns:
        The path to the saved markdown file.
    """
    html = fetch_content_html(node.path_id)
    output_dir = _get_output_dir(node)
    markdown = html_to_markdown(html, md_file_dir=output_dir)
    return _write_markdown(node, markdown, output_dir)


def scrape_all(
    force: bool = False,
    progress: ProgressCallback | None = None,
) -> dict[str, int]:
    """Scrape all pages, or only updated ones.

    Args:
        force: If True, re-scrape every page regardless of update status.
        progress: Optional callback for progress updates.

    Returns:
        A dict with counts: updated, added, removed, total, skipped.
    """
    checker = UpdateChecker()

    if force:
        pages = flatten_catalog(get_catalog_tree())
        to_update = pages
        to_add: list[CatalogNode] = []
        to_remove: list[str] = []
    else:
        to_update, to_add, to_remove = checker.check_updates()

    all_to_scrape = to_update + to_add
    total = len(all_to_scrape)

    stats = {
        "updated": len(to_update),
        "added": len(to_add),
        "removed": len(to_remove),
        "total": total,
        "skipped": 0,
        "errors": 0,
    }

    counter = {"value": 0}
    counter_lock = threading.Lock()

    def _scrape_one(node: CatalogNode) -> None:
        try:
            scrape_page(node)
            checker.record_page(node)
        except Exception as exc:
            with counter_lock:
                stats["errors"] += 1
            print(f"[ERROR] {node.title} ({node.path_id}): {exc}")
        finally:
            with counter_lock:
                counter["value"] += 1
                if progress:
                    progress(counter["value"], total, node.title)

    if total > 0:
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(_scrape_one, node) for node in all_to_scrape]
            for future in as_completed(futures):
                future.result()

    # Remove pages that no longer exist
    for path_id in to_remove:
        # Try to find and remove the old md file
        stored = checker._state.get("pages", {}).get(path_id, {})
        cat_path = stored.get("category_path", "")
        title = stored.get("title", "")
        if cat_path and title:
            old_file = get_docs_dir().joinpath(
                *cat_path.split("/"), get_safe_filename(title)
            )
            if old_file.exists():
                old_file.unlink()
        checker.remove_page(path_id)

    checker.save_state()

    # Calculate skipped (pages that didn't change)
    if not force:
        all_pages = flatten_catalog(get_catalog_tree())
        stats["skipped"] = len(all_pages) - total

    return stats


def list_categories() -> list[str]:
    """Return a sorted list of all top-level categories."""
    tree = get_catalog_tree()
    return sorted({node.title for node in tree})


def generate_index() -> Path:
    """Generate an index.md file listing all scraped pages by category."""
    from src.core.config import get_language

    tree = get_catalog_tree()
    lang = get_language()
    if lang.value == "zh-cn":
        title_line = "# 原神千星奇域·综合指南 文档索引\n"
    else:
        title_line = "# Genshin Impact Miliastra Wonderland - General Guide Index\n"
    lines: list[str] = [title_line]

    def _walk(node: CatalogNode, depth: int) -> None:
        indent = "  " * depth
        if node.is_category:
            lines.append(f"{indent}- **{node.title}**")
            for child in node.children:
                _walk(child, depth + 1)
        else:
            filename = get_safe_filename(node.title)
            cat_path = node.category_path.replace("/", "/")
            rel_link = f"{cat_path}/{filename}" if cat_path else filename
            lines.append(f"{indent}- [{node.title}]({rel_link})")

    for node in tree:
        _walk(node, 0)

    index_path = get_docs_dir() / "index.md"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return index_path
