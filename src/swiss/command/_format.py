"""Format the given source directory."""

import logging
import subprocess
import sys
from argparse import ArgumentParser, Namespace, _SubParsersAction

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class FormatCommand(BaseCommand):
    """Class for the format command."""

    NAME = "format"
    DESCRIPTION = "Format the given source directory."

    def __init__(self) -> None:
        """Constructor for FormatCommand."""
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
            help="The source directories to format.",
            nargs="+",
        )
        swing_parser.set_defaults(func=self._handle_format)

    def _handle_format(self, args: Namespace) -> bool:
        """Handle the format sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        returncode = 0

        _LOGGER.info("Formatting sources.")
        for source in args.source:
            _LOGGER.info(f"\Formatting {source}.")
            returncode += subprocess.run(
                [sys.executable, "-m", "black", source]
            ).returncode

            returncode += subprocess.run(
                [sys.executable, "-m", "isort", source]
            ).returncode
        _LOGGER.info("Done formatting sources.")

        return returncode == 0
