"""Update detection logic based on the update log and timestamps."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from src.core.config import get_state_file
from src.scraper.catalog import CatalogNode, flatten_catalog, get_catalog_tree


class UpdateChecker:
    """Detect which pages have been updated since the last scrape.

    The scraper stores a state file (.scraper_state.json) that records
    the `updated_at` timestamp of every page. On each run, the checker
    compares the current catalog timestamps against the stored state
    to determine which pages need to be re-scraped.
    """

    def __init__(self, state_file: Path | None = None) -> None:
        self._state_file = state_file or get_state_file()
        self._state: dict[str, Any] = self._load_state()

    def _load_state(self) -> dict[str, Any]:
        """Load the previous scrape state from disk."""
        if not self._state_file.exists():
            return {"pages": {}, "last_run": None}
        try:
            with open(self._state_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {"pages": {}, "last_run": None}

    def save_state(self) -> None:
        """Persist the current state to disk."""
        self._state["last_run"] = datetime.now().isoformat()
        self._state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self._state_file, "w", encoding="utf-8") as f:
            json.dump(self._state, f, ensure_ascii=False, indent=2)

    def get_stored_updated_at(self, path_id: str) -> str | None:
        """Return the stored updated_at timestamp for a page, or None."""
        return self._state.get("pages", {}).get(path_id, {}).get("updated_at")

    def record_page(self, node: CatalogNode) -> None:
        """Record a page's metadata in the state after scraping."""
        self._state.setdefault("pages", {})[node.path_id] = {
            "title": node.title,
            "updated_at": node.updated_at,
            "category_path": node.category_path,
            "scraped_at": datetime.now().isoformat(),
        }

    def remove_page(self, path_id: str) -> None:
        """Remove a page from state (e.g. when it no longer exists)."""
        self._state.get("pages", {}).pop(path_id, None)

    def check_updates(
        self,
    ) -> tuple[list[CatalogNode], list[CatalogNode], list[str]]:
        """Compare the current catalog against stored state.

        Returns:
            A tuple of (to_update, to_add, to_remove):
            - to_update: pages whose updated_at has changed (need re-scrape)
            - to_add: new pages not in state
            - to_remove: path_ids in state but no longer in the catalog
        """
        tree = get_catalog_tree()
        all_pages = flatten_catalog(tree)
        current_ids = {node.path_id for node in all_pages}

        stored_ids = set(self._state.get("pages", {}).keys())

        to_update: list[CatalogNode] = []
        to_add: list[CatalogNode] = []

        for node in all_pages:
            stored_ts = self.get_stored_updated_at(node.path_id)
            if stored_ts is None:
                to_add.append(node)
            elif stored_ts != node.updated_at:
                to_update.append(node)

        to_remove = list(stored_ids - current_ids)

        return to_update, to_add, to_remove

    def get_all_current_pages(self) -> list[CatalogNode]:
        """Return all pages from the current catalog."""
        tree = get_catalog_tree()
        return flatten_catalog(tree)


def parse_update_log_pages(update_log_html: str) -> list[str]:
    """Parse the update log page content to extract linked page IDs.

    The update log (更新日志) lists pages that were added or modified.
    This helper extracts path_ids from links in the update log content.

    Args:
        update_log_html: The raw HTML of the update log page.

    Returns:
        A list of path_ids referenced in the update log.
    """
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(update_log_html, "html.parser")
    ids: list[str] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Links look like /ys/ugc/tutorial//detail/{path_id} or /detail/{path_id}
        match = href.split("/detail/")[-1] if "/detail/" in href else ""
        if match and len(match) > 5:
            ids.append(match)
    return ids
