import os
from pathlib import Path

import pytest
from click.testing import CliRunner

from second_brain.app import main


@pytest.fixture()
def brain_path(tmp_path, monkeypatch):
    path = tmp_path / "second_brain"
    monkeypatch.setenv("BRAIN_PATH", str(path))
    return path


def test_new_creates_file(brain_path):
    runner = CliRunner()
    result = runner.invoke(main, ["new", "My brilliant idea about caching"])
    assert result.exit_code == 0
    files = list(brain_path.glob("*.md"))
    assert len(files) == 1


def test_new_file_content(brain_path):
    runner = CliRunner()
    runner.invoke(main, ["new", "My brilliant idea about caching"])
    files = list(brain_path.glob("*.md"))
    assert files[0].read_text() == "My brilliant idea about caching"


def test_new_creates_brain_dir_if_missing(tmp_path, monkeypatch):
    path = tmp_path / "does_not_exist" / "brain"
    monkeypatch.setenv("BRAIN_PATH", str(path))
    runner = CliRunner()
    result = runner.invoke(main, ["new", "hello"])
    assert result.exit_code == 0
    assert path.exists()


def test_new_filename_is_timestamp_based(brain_path):
    """Filename should match YYYYMMDD_HHMMSS.md pattern."""
    runner = CliRunner()
    runner.invoke(main, ["new", "a thought"])
    files = list(brain_path.glob("*.md"))
    name = files[0].stem
    # stem must be 15 chars: YYYYMMDD_HHMMSS
    assert len(name) == 15
    assert name[8] == "_"
    assert name[:8].isdigit()
    assert name[9:].isdigit()


def test_new_default_brain_path(tmp_path, monkeypatch):
    """When BRAIN_PATH is not set, defaults to ~/second_brain/."""
    monkeypatch.delenv("BRAIN_PATH", raising=False)
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setenv("HOME", str(fake_home))
    runner = CliRunner()
    result = runner.invoke(main, ["new", "default path test"])
    assert result.exit_code == 0
    assert (fake_home / "second_brain").exists()


def test_new_prints_saved_path(brain_path):
    runner = CliRunner()
    result = runner.invoke(main, ["new", "check output"])
    assert str(brain_path) in result.output


def test_main_no_args_shows_help():
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0
    assert "new" in result.output
