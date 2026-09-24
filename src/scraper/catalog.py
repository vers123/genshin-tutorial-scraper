"""Fetch and parse the tutorial catalog (directory tree)."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any

import requests

from src.core.config import (
    Language,
    MAX_RETRIES,
    REQUEST_TIMEOUT,
    RETRY_DELAY,
    get_catalog_url,
    get_language,
    get_request_headers,
    get_text_map_url,
)


@dataclass
class CatalogNode:
    """A node in the tutorial catalog tree."""

    title: str
    path_id: str
    real_id: str
    updated_at: str
    doc_type: str
    article_type: int | None = None
    video_poster: str | None = None
    children: list["CatalogNode"] = field(default_factory=list)
    parent: "CatalogNode | None" = None
    catalog_path_id: str = ""
    """The original path_id from the catalog (before English remapping)."""

    @property
    def is_category(self) -> bool:
        """Whether this node is a category (has children)."""
        return len(self.children) > 0

    @property
    def breadcrumb(self) -> list[str]:
        """Return the breadcrumb path from root to this node."""
        path: list[str] = []
        node: CatalogNode | None = self
        while node is not None:
            path.append(node.title)
            node = node.parent
        path.reverse()
        return path

    @property
    def category_path(self) -> str:
        """Return the category path as a forward-slash separated string."""
        crumbs = self.breadcrumb
        # The first element is the root category; the last is the page itself.
        # For category path, we use all but the last (the page title).
        if len(crumbs) <= 1:
            return crumbs[0]
        return "/".join(crumbs[:-1])


def _request_with_retry(url: str) -> requests.Response:
    """Perform a GET request with retry logic."""
    last_exc: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(
                url, headers=get_request_headers(), timeout=REQUEST_TIMEOUT
            )
            resp.raise_for_status()
            return resp
        except requests.RequestException as exc:
            last_exc = exc
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY * attempt)
    raise RuntimeError(f"Failed to fetch {url} after {MAX_RETRIES} attempts: {last_exc}")


def fetch_catalog_json() -> list[dict[str, Any]]:
    """Fetch the raw catalog JSON from the website."""
    resp = _request_with_retry(get_catalog_url())
    return resp.json()


def fetch_text_map() -> dict[str, str]:
    """Fetch the textMap JSON (used to resolve English path_ids).

    For the English version, the catalog path_ids are the *Chinese* ids and
    do not match the actual English content files. The textMap.json lists the
    real English path_ids in the same order as the (flattened) catalog, so we
    can remap them positionally.
    """
    resp = _request_with_retry(get_text_map_url())
    return resp.json()


def _remap_english_path_ids(
    nodes: list[CatalogNode], text_map: dict[str, str]
) -> None:
    """Replace catalog path_ids with the real English content path_ids.

    The English catalog shares the Chinese path_ids, but the actual English
    content.html files are stored under different ids. The textMap.json keys
    are the real English ids, ordered to match the flattened catalog.
    """
    en_ids = list(text_map.keys())

    flat: list[CatalogNode] = []

    def _walk(node: CatalogNode) -> None:
        flat.append(node)
        for child in node.children:
            _walk(child)

    for node in nodes:
        _walk(node)

    for i, node in enumerate(flat):
        if i < len(en_ids):
            node.path_id = en_ids[i]
            node.real_id = en_ids[i]
            # catalog_path_id keeps the original catalog id for lookups


def parse_catalog(data: list[dict[str, Any]]) -> list[CatalogNode]:
    """Parse the raw catalog JSON into a tree of CatalogNode objects."""
    nodes: list[CatalogNode] = []

    def _build(item: dict[str, Any], parent: CatalogNode | None = None) -> CatalogNode:
        orig_id = item.get("path_id", "")
        node = CatalogNode(
            title=item.get("title", ""),
            path_id=orig_id,
            real_id=item.get("real_id", orig_id),
            updated_at=item.get("updated_at", ""),
            doc_type=item.get("doc_type", "document"),
            article_type=item.get("article_type"),
            video_poster=item.get("videoPoster"),
            parent=parent,
            catalog_path_id=orig_id,
        )
        for child in item.get("children", []) or []:
            node.children.append(_build(child, node))
        return node

    for item in data:
        nodes.append(_build(item))
    return nodes


def flatten_catalog(nodes: list[CatalogNode]) -> list[CatalogNode]:
    """Flatten the catalog tree into a list of all leaf/document nodes."""
    result: list[CatalogNode] = []

    def _walk(node: CatalogNode) -> None:
        if not node.is_category:
            result.append(node)
        for child in node.children:
            _walk(child)

    for node in nodes:
        _walk(node)
    return result


def get_catalog_tree() -> list[CatalogNode]:
    """Fetch and parse the catalog, returning the full tree.

    For the English language, the catalog path_ids are remapped to the real
    English content ids (resolved via textMap.json) so that downstream code
    can fetch content.html directly.
    """
    data = fetch_catalog_json()
    tree = parse_catalog(data)
    if get_language() is Language.EN_US:
        try:
            text_map = fetch_text_map()
            _remap_english_path_ids(tree, text_map)
        except Exception as exc:
            print(f"[WARN] Failed to remap English path_ids: {exc}")
    return tree


def get_all_pages() -> list[CatalogNode]:
    """Fetch the catalog and return a flat list of all document pages."""
    tree = get_catalog_tree()
    return flatten_catalog(tree)
