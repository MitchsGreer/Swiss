"""Command line utilities."""

from swiss.cli import CLI


def main() -> None:
    """Main entry point."""
    cli = CLI()
    cli.run()
