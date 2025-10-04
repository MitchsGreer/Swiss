"""Command line utilities."""

from swiss.cli import CLI


def main() -> None:
    """Run the main applications."""
    cli = CLI()
    cli.run()
