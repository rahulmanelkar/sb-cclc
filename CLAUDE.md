# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**second-brain** — a Python CLI for capturing quick thoughts as markdown notes. Built with Click, uses loguru for logging, managed with uv.

Requires Python >= 3.13.

## Commands

```bash
# Run tests
uv run pytest
uv run pytest --cov                  # with coverage (must stay >= 80%)
uv run pytest tests/test_notes.py -k "test_slugify"  # single test

# Lint and format
uv run ruff check .
uv run ruff format .

# Run the CLI
uv run second_brain new "My idea"
uv run second_brain list
uv run second_brain show 1

# Docs
uv run python scripts/serve_docs.py  # local dev server
uv run mkdocs build                  # static build
```

## Architecture

Three source modules with a strict dependency chain (no circular deps):

```
__main__.py → cli.py → app.py      (logging config)
                     → notes.py    (pure note logic)
```

- **`notes.py`** — Pure business logic. Slugifies titles, builds date-prefixed paths (`YYYY-MM-DD-slug.md`), handles duplicate filenames with `-1`, `-2` suffixes, writes markdown files. No third-party deps.
- **`app.py`** — Logging setup only (loguru). Console output to stderr with compact 3-letter levels, file output with rotation.
- **`cli.py`** — Click command group (`new`, `list`, `show`). Reads `SECOND_BRAIN_DIR` env var (default: `~/second_brain/`). All configuration is via environment variables, no config files.

## Testing

- Tests use real file I/O via pytest `tmp_path` — no mocking.
- `conftest.py` provides `tmp_note_dir` fixture (sets `SECOND_BRAIN_DIR` to a temp dir) and auto-redirects `LOG_FILE`.
- CLI tests use Click's `CliRunner` for integration testing.
- pytest-env loads `.env.test` automatically.
- Import mode is `importlib` (configured in pyproject.toml).

## Code Style

- ruff: line-length 88, target py313, double quotes
- Lint rules: E, F, B, I, UP (E501 ignored)
- Docstrings: Google style (used by mkdocstrings for API docs)
