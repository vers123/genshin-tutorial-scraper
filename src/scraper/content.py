"""Fetch the raw HTML content for a tutorial page."""

from __future__ import annotations

import time

import requests

from src.core.config import (
    CONTENT_URL_TEMPLATE,
    MAX_RETRIES,
    REQUEST_HEADERS,
    REQUEST_TIMEOUT,
    RETRY_DELAY,
)


def _request_with_retry(url: str) -> requests.Response:
    """Perform a GET request with retry logic."""
    last_exc: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(
                url, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT
            )
            resp.raise_for_status()
            return resp
        except requests.RequestException as exc:
            last_exc = exc
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY * attempt)
    raise RuntimeError(f"Failed to fetch {url} after {MAX_RETRIES} attempts: {last_exc}")


def fetch_content_html(path_id: str) -> str:
    """Fetch the raw HTML content for a given page path_id.

    Args:
        path_id: The unique page identifier from the catalog.

    Returns:
        The raw HTML string of the page content.
    """
    url = CONTENT_URL_TEMPLATE.format(path_id=path_id)
    resp = _request_with_retry(url)
    # The content is served as UTF-8; ensure correct decoding.
    resp.encoding = "utf-8"
    return resp.text
