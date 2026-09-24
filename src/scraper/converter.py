"""Convert tutorial HTML content to Markdown."""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Callable

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

from src.core.config import MAX_WORKERS
from src.scraper.images import download_image, get_relative_image_path


class TutorialConverter(MarkdownConverter):
    """Custom markdown converter for tutorial content.

    Handles images (downloads them locally and rewrites paths),
    videos, and other tutorial-specific elements.
    """

    def __init__(
        self,
        *,
        md_file_dir: Path,
        image_map: dict[str, Path | None] | None = None,
        image_callback: Callable[[str], Path | None] | None = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._md_file_dir = md_file_dir
        self._image_map = image_map or {}
        self._image_callback = image_callback

    def _get_local_path(self, src: str) -> Path | None:
        """Look up the local path for an image URL, falling back to callback."""
        if src in self._image_map:
            return self._image_map[src]
        if self._image_callback:
            return self._image_callback(src)
        return download_image(src)

    def convert_img(self, el, text, parent_tags):
        """Convert <img> tags, downloading images locally."""
        src = el.get("src", "")
        alt = el.get("alt", "")
        title = el.get("title", "")

        if not src:
            return ""

        # Handle protocol-relative URLs
        if src.startswith("//"):
            src = "https:" + src

        local_path = self._get_local_path(src)
        if local_path is not None:
            rel_path = get_relative_image_path(local_path, self._md_file_dir)
            img_md = f"![{alt}]({rel_path})"
        else:
            # Fallback to remote URL if download fails
            img_md = f"![{alt}]({src})"

        if title:
            img_md = img_md[:-1] + f' "{title}")'

        return img_md

    def convert_video(self, el, text, parent_tags):
        """Convert <video> tags to a markdown link/description."""
        src = el.get("src", "")
        poster = el.get("poster", "")
        # Try to find a <source> child
        source = el.find("source")
        if source and source.get("src"):
            src = source.get("src", src)

        if not src:
            return text

        if src.startswith("//"):
            src = "https:" + src

        poster_md = ""
        if poster:
            if poster.startswith("//"):
                poster = "https:" + poster
            local_poster = self._image_callback(poster)
            if local_poster:
                rel_poster = get_relative_image_path(
                    local_poster, self._md_file_dir
                )
                poster_md = f"![video poster]({rel_poster})\\n"

        return f"{poster_md}[🎬 视频]({src})"

    def convert_span(self, el, text, parent_tags):
        """Convert <span> tags (used for colored/styled text in tutorials)."""
        # Preserve the text content; styling info is lost in plain markdown.
        return text

    def convert_div(self, el, text, parent_tags):
        """Convert <div> tags."""
        return text

    def convert_table(self, el, text, parent_tags):
        """Convert tables to markdown tables."""
        return super().convert_table(el, text, parent_tags)


def _sanitize_filename(name: str) -> str:
    """Sanitize a string for use as a filename."""
    # Remove or replace characters that are invalid in filenames
    name = re.sub(r'[\\/:*?"<>|]', "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    # Truncate to a reasonable length
    if len(name) > 80:
        name = name[:80].rstrip()
    return name


def _extract_image_urls(soup: BeautifulSoup) -> list[str]:
    """Extract all image URLs from the parsed HTML."""
    urls: set[str] = set()
    for img in soup.find_all("img", src=True):
        src = img["src"]
        if src.startswith("//"):
            src = "https:" + src
        if src.startswith(("http://", "https://")):
            urls.add(src)
    # Also check video posters
    for video in soup.find_all("video", poster=True):
        poster = video["poster"]
        if poster.startswith("//"):
            poster = "https:" + poster
        if poster.startswith(("http://", "https://")):
            urls.add(poster)
    return list(urls)


def _download_images_concurrently(urls: list[str]) -> dict[str, Path | None]:
    """Download multiple images concurrently and return a URL->path map."""
    if not urls:
        return {}
    result: dict[str, Path | None] = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(download_image, url): url for url in urls}
        for future in futures:
            url = futures[future]
            try:
                result[url] = future.result()
            except Exception:
                result[url] = None
    return result


def html_to_markdown(
    html: str,
    md_file_dir: Path,
    image_callback: Callable[[str], Path | None] | None = None,
) -> str:
    """Convert tutorial HTML content to Markdown.

    Args:
        html: The raw HTML content string.
        md_file_dir: The directory where the markdown file will be saved
                     (used to compute relative image paths).
        image_callback: Optional callback to download images. If None,
                        images are downloaded concurrently using the default
                        download_image function.

    Returns:
        The converted Markdown string.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style tags
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()

    # Pre-download all images concurrently for speed
    image_map: dict[str, Path | None] | None = None
    if image_callback is None:
        image_urls = _extract_image_urls(soup)
        image_map = _download_images_concurrently(image_urls)

    converter = TutorialConverter(
        md_file_dir=md_file_dir,
        image_map=image_map,
        image_callback=image_callback,
        heading_style="ATX",
        bullets="-",
        strong_em_symbol="*",
    )
    markdown = converter.convert_soup(soup)

    # Clean up excessive blank lines (more than 2 consecutive newlines)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)

    return markdown.strip() + "\n"


def get_safe_filename(title: str) -> str:
    """Get a safe markdown filename from a page title."""
    return f"{_sanitize_filename(title)}.md"
