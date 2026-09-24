"""Download images referenced in tutorial content."""

from __future__ import annotations

import hashlib
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

from src.core.config import (
    MAX_RETRIES,
    REQUEST_TIMEOUT,
    RETRY_DELAY,
    get_images_dir,
    get_request_headers,
)


def _url_to_filename(url: str) -> str:
    """Convert an image URL to a safe local filename.

    Uses a hash of the URL plus the original extension to avoid name collisions
    and keep file paths short.
    """
    parsed = urlparse(url)
    ext = Path(parsed.path).suffix or ".png"
    # Limit extension length to avoid weird cases
    if len(ext) > 10:
        ext = ".png"
    url_hash = hashlib.md5(url.encode("utf-8")).hexdigest()[:16]
    return f"{url_hash}{ext}"


def download_image(url: str, output_dir: Path | None = None) -> Path | None:
    """Download an image and return its local path.

    Args:
        url: The image URL to download.
        output_dir: Directory to save the image. Defaults to IMAGES_DIR.

    Returns:
        The local path of the downloaded image, or None if download failed.
    """
    if not url or not url.startswith(("http://", "https://")):
        return None

    if output_dir is None:
        output_dir = get_images_dir()
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = _url_to_filename(url)
    local_path = output_dir / filename

    # Skip if already downloaded
    if local_path.exists() and local_path.stat().st_size > 0:
        return local_path

    last_exc: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(
                url, headers=get_request_headers(), timeout=REQUEST_TIMEOUT, stream=True
            )
            resp.raise_for_status()
            with open(local_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            return local_path
        except (requests.RequestException, OSError) as exc:
            last_exc = exc
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY * attempt)

    print(f"[WARN] Failed to download image: {url} ({last_exc})")
    return None


def get_relative_image_path(local_path: Path, md_file_dir: Path) -> str:
    """Compute the relative path from a markdown file's directory to an image.

    Args:
        local_path: The absolute path of the downloaded image.
        md_file_dir: The directory containing the markdown file.

    Returns:
        A relative path string suitable for use in markdown image syntax.
    """
    try:
        rel = local_path.resolve().relative_to(md_file_dir.resolve())
        return str(rel).replace("\\", "/")
    except ValueError:
        # If the image is outside the md file's directory, compute relative path
        rel = Path(local_path).resolve()
        base = md_file_dir.resolve()
        # Use os.path.relpath for cross-directory relative paths
        import os

        return os.path.relpath(rel, base).replace("\\", "/")
