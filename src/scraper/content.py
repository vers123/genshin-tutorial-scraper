"""Fetch the raw HTML content for a tutorial page."""

from __future__ import annotations

import time

import requests

from src.core.config import (
    MAX_RETRIES,
    REQUEST_TIMEOUT,
    RETRY_DELAY,
    get_content_url_template,
    get_request_headers,
)


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


def fetch_content_html(path_id: str) -> str:
    """Fetch the raw HTML content for a given page path_id.

    Args:
        path_id: The unique page identifier from the catalog.

    Returns:
        The raw HTML string of the page content.
    """
    url = get_content_url_template().format(path_id=path_id)
    resp = _request_with_retry(url)
    # The content is served as UTF-8; ensure correct decoding.
    resp.encoding = "utf-8"
    return resp.text
