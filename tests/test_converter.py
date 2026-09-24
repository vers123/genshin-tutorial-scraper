"""Tests for the HTML-to-Markdown converter."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

from src.scraper.converter import get_safe_filename, html_to_markdown


def test_get_safe_filename():
    assert get_safe_filename("测试页面") == "测试页面.md"
    assert get_safe_filename("a/b:c*d?e") == "a_b_c_d_e.md"
    assert get_safe_filename("  trim  ") == "trim.md"


def test_html_to_markdown_headings(tmp_path: Path):
    html = "<h1>Title</h1><p>Hello world</p>"
    md = html_to_markdown(html, md_file_dir=tmp_path)
    assert "# Title" in md
    assert "Hello world" in md


def test_html_to_markdown_lists(tmp_path: Path):
    html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
    md = html_to_markdown(html, md_file_dir=tmp_path)
    assert "- Item 1" in md
    assert "- Item 2" in md


def test_html_to_markdown_table(tmp_path: Path):
    html = (
        "<table>"
        "<tr><th>Header 1</th><th>Header 2</th></tr>"
        "<tr><td>Cell 1</td><td>Cell 2</td></tr>"
        "</table>"
    )
    md = html_to_markdown(html, md_file_dir=tmp_path)
    assert "Header 1" in md
    assert "Cell 1" in md


def test_html_to_markdown_strips_scripts(tmp_path: Path):
    html = "<p>Visible</p><script>alert('x')</script>"
    md = html_to_markdown(html, md_file_dir=tmp_path)
    assert "Visible" in md
    assert "alert" not in md


def test_html_to_markdown_image_no_download(tmp_path: Path):
    """When image download is mocked, use the local path."""
    html = '<p><img src="https://example.com/img.png" alt="test"></p>'
    mock_img = tmp_path / "abc123.png"
    mock_img.write_bytes(b"fake")
    callback = MagicMock(return_value=mock_img)
    md = html_to_markdown(html, md_file_dir=tmp_path, image_callback=callback)
    assert "![test]" in md
    callback.assert_called_once_with("https://example.com/img.png")


def test_html_to_markdown_image_download_failure(tmp_path: Path):
    """When image download fails, fall back to remote URL."""
    html = '<p><img src="https://example.com/img.png" alt="test"></p>'
    callback = MagicMock(return_value=None)
    md = html_to_markdown(html, md_file_dir=tmp_path, image_callback=callback)
    assert "![test](https://example.com/img.png)" in md
