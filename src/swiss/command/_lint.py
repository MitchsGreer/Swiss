"""Lint the given source directories."""

import logging
import subprocess
import sys
from argparse import ArgumentParser, Namespace, _SubParsersAction

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class LintCommand(BaseCommand):
    """Class for the lint command."""

    NAME = "lint"
    DESCRIPTION = "Lint the given source directories."

    def __init__(self) -> None:
        """Constructor for LintCommand."""
        super().__init__(self.NAME, self.DESCRIPTION)

    def add_to_parser(self, root_parser: _SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
        swing_parser: ArgumentParser = root_parser.add_parser(
            self.name, help=self.description
        )
        swing_parser.add_argument(
            "source",
            metavar="SOURCE",
            help="The python sources to lint.",
            nargs="+",
        )
        swing_parser.set_defaults(func=self._handle_lint)

    def _handle_lint(self, args: Namespace) -> bool:
        """Handle the lint sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        returncode = 0

        _LOGGER.info("Linting sources.")
        for source in args.source:
            _LOGGER.info(f"\Linting {source}.")
            returncode += subprocess.run(
                [sys.executable, "-m", "ruff", source]
            ).returncode
        _LOGGER.info("Done Linting sources.")

        return returncode == 0
