# second-brain

## Installation

Clone the repository and install dependencies:

```bash
git clone <repo-url>
cd second-brain
uv sync
```

## Usage

Save a quick thought:

```bash
second_brain new "My brilliant idea about caching"
# Saved: /home/user/second_brain/20260322_153045.md
```

Notes are saved as plain markdown files with a timestamp filename (`YYYYMMDD_HHMMSS.md`).

Via the module:

```bash
uv run python -m second_brain new "My brilliant idea"
```

## Configuration

`second_brain` reads `~/.env` on startup. Set `BRAIN_PATH` to control where notes are stored.

```dotenv
# ~/.env
BRAIN_PATH=/home/user/notes/second_brain
```

| Variable     | Default           | Description                                         |
|--------------|-------------------|-----------------------------------------------------|
| `BRAIN_PATH` | `~/second_brain/` | Directory where markdown notes are saved.           |
| `LOG_LEVEL`  | `INFO`            | Console log level. Set to `DEBUG` for verbose output. |
| `LOG_FILE`   | `app.log`         | Path to the log file.                               |

## Testing

Run tests:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov
```

## Documentation

Preview docs locally:

```bash
uv run python scripts/serve_docs.py
```

Build static docs:

```bash
uv run mkdocs build
```
