"""Tests for the catalog parser."""

from __future__ import annotations

from src.scraper.catalog import (
    CatalogNode,
    flatten_catalog,
    parse_catalog,
)


SAMPLE_CATALOG = [
    {
        "updated_at": "2026-09-20 11:11:51",
        "title": "更新日志",
        "path_id": "mhs2w008wf14",
        "real_id": "mhs2w008wf14",
        "children": [],
        "doc_type": "document",
    },
    {
        "updated_at": "2025-09-19 18:47:23",
        "title": "界面介绍",
        "path_id": "mhz71urk21nq",
        "real_id": "mhz71urk21nq",
        "children": [
            {
                "updated_at": "2025-10-24 10:33:06",
                "title": "整体界面",
                "path_id": "mhn4bsi5lb58",
                "real_id": "mhn4bsi5lb58",
                "children": [],
                "article_type": 8,
                "doc_type": "document",
            },
            {
                "updated_at": "2026-07-10 16:24:01",
                "title": "地形编辑",
                "path_id": "mhwe1n94b1x6",
                "real_id": "mhwe1n94b1x6",
                "children": [],
                "doc_type": "document",
            },
        ],
        "article_type": 8,
        "doc_type": "document",
    },
]


def test_parse_catalog_basic():
    nodes = parse_catalog(SAMPLE_CATALOG)
    assert len(nodes) == 2
    assert nodes[0].title == "更新日志"
    assert nodes[0].path_id == "mhs2w008wf14"
    assert not nodes[0].is_category


def test_parse_catalog_children():
    nodes = parse_catalog(SAMPLE_CATALOG)
    intro = nodes[1]
    assert intro.title == "界面介绍"
    assert intro.is_category
    assert len(intro.children) == 2
    assert intro.children[0].title == "整体界面"
    assert intro.children[0].parent is intro


def test_flatten_catalog():
    nodes = parse_catalog(SAMPLE_CATALOG)
    flat = flatten_catalog(nodes)
    titles = {n.title for n in flat}
    assert "更新日志" in titles
    assert "整体界面" in titles
    assert "地形编辑" in titles
    # Category node itself should not appear as a leaf
    assert "界面介绍" not in titles
    assert len(flat) == 3


def test_breadcrumb():
    nodes = parse_catalog(SAMPLE_CATALOG)
    flat = flatten_catalog(nodes)
    zhengti = next(n for n in flat if n.title == "整体界面")
    assert zhengti.breadcrumb == ["界面介绍", "整体界面"]
    assert zhengti.category_path == "界面介绍"


def test_catalog_node_properties():
    node = CatalogNode(
        title="测试", path_id="test123", real_id="test123",
        updated_at="2026-01-01 00:00:00", doc_type="document",
    )
    assert not node.is_category
    assert node.breadcrumb == ["测试"]
    assert node.category_path == "测试"
