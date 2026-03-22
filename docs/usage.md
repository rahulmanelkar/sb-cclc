# Usage

## Installation

Clone the repository and install dependencies:

```bash
uv sync
```

## Running

Via the CLI entrypoint:

```bash
uv run second_brain                          # show help
uv run second_brain new "My brilliant idea" # save a note
```

Or as a Python module:

```bash
uv run python -m second_brain new "My brilliant idea"
```

## Commands

### `second_brain new TEXT`

Saves `TEXT` as a plain markdown file in `BRAIN_PATH`.

The filename is a timestamp in the format `YYYYMMDD_HHMMSS.md`.

```bash
second_brain new "My brilliant idea about caching"
# Saved: /home/user/second_brain/20260322_153045.md
```

## Environment Variables

`second_brain` reads `~/.env` on startup. Set `BRAIN_PATH` there to configure
the storage location, or export it in your shell.

| Variable     | Default              | Description                              |
|--------------|----------------------|------------------------------------------|
| `BRAIN_PATH` | `~/second_brain/`    | Directory where notes are stored         |
| `LOG_LEVEL`  | `INFO`               | Console log level (DEBUG, INFO, …)       |
| `LOG_FILE`   | `app.log`            | Path to the log file                     |

Example `~/.env`:

```dotenv
BRAIN_PATH=/home/user/notes/second_brain
LOG_LEVEL=INFO
```
