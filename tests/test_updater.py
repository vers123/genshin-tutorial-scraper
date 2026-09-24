"""Tests for the update checker."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

from src.core.updater import UpdateChecker
from src.scraper.catalog import CatalogNode


def _make_node(title="test", path_id="test123", updated_at="2026-01-01 00:00:00"):
    return CatalogNode(
        title=title,
        path_id=path_id,
        real_id=path_id,
        updated_at=updated_at,
        doc_type="document",
    )


def test_checker_loads_empty_state(tmp_path: Path):
    state_file = tmp_path / "state.json"
    checker = UpdateChecker(state_file=state_file)
    assert checker._state == {"pages": {}, "last_run": None}


def test_checker_record_and_save(tmp_path: Path):
    state_file = tmp_path / "state.json"
    checker = UpdateChecker(state_file=state_file)
    node = _make_node()
    checker.record_page(node)
    checker.save_state()
    assert state_file.exists()
    data = json.loads(state_file.read_text(encoding="utf-8"))
    assert "test123" in data["pages"]
    assert data["pages"]["test123"]["updated_at"] == "2026-01-01 00:00:00"


def test_checker_get_stored_updated_at(tmp_path: Path):
    state_file = tmp_path / "state.json"
    checker = UpdateChecker(state_file=state_file)
    node = _make_node()
    checker.record_page(node)
    assert checker.get_stored_updated_at("test123") == "2026-01-01 00:00:00"
    assert checker.get_stored_updated_at("nonexistent") is None


def test_checker_remove_page(tmp_path: Path):
    state_file = tmp_path / "state.json"
    checker = UpdateChecker(state_file=state_file)
    node = _make_node()
    checker.record_page(node)
    checker.remove_page("test123")
    assert checker.get_stored_updated_at("test123") is None


def test_checker_corrupt_state(tmp_path: Path):
    state_file = tmp_path / "state.json"
    state_file.write_text("not json", encoding="utf-8")
    checker = UpdateChecker(state_file=state_file)
    assert checker._state == {"pages": {}, "last_run": None}
