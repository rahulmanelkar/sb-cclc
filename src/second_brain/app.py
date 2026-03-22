import os
import sys
from datetime import datetime
from pathlib import Path

import click
from dotenv import load_dotenv
from loguru import logger


def configure_logging():
    """Configure loguru for console and file logging.

    Removes the default handler and sets up:
    - stderr handler at LOG_LEVEL (default: INFO, configurable via env var)
    - File handler at DEBUG level writing to LOG_FILE (default: app.log)
    """
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    log_file = os.environ.get("LOG_FILE", "app.log")
    logger.remove()
    logger.add(sys.stderr, level=log_level)
    logger.add(log_file, level="DEBUG", rotation="50 KB", retention=1)


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """second_brain — save quick thoughts from the command line."""
    load_dotenv(Path.home() / ".env")
    configure_logging()
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command()
@click.argument("text")
def new(text):
    """Save TEXT as a new markdown note."""
    brain_path = Path(os.environ.get("BRAIN_PATH", Path.home() / "second_brain"))
    brain_path.mkdir(parents=True, exist_ok=True)

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".md"
    filepath = brain_path / filename
    filepath.write_text(text)

    click.echo(f"Saved: {filepath}")
    logger.info(f"Saved note to {filepath}")
