"""Format the given source directory."""

import logging
import subprocess
from argparse import ArgumentParser, Namespace, _SubParsersAction

from swiss.util import find_command_path

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class FormatCommand(BaseCommand):
    """Class for the format command."""

    NAME = "format"
    DESCRIPTION = "Format the given source directory."

    def __init__(self: "FormatCommand") -> None:
        """Constructor for FormatCommand."""
        super().__init__(self.NAME, self.DESCRIPTION)

    def add_to_parser(self: "FormatCommand", root_parser: _SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
        swing_parser: ArgumentParser = root_parser.add_parser(self.name, help=self.description)
        swing_parser.add_argument(
            "source",
            metavar="SOURCE",
            help="The source directories to format.",
            nargs="+",
        )
        swing_parser.set_defaults(func=self._handle_format)

    def _handle_format(self: "FormatCommand", args: Namespace) -> bool:
        """Handle the format sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        returncode = 0

        _LOGGER.info("Formatting sources.")
        for source in args.source:
            _LOGGER.info(f"\tFormatting {source}.")
            returncode += subprocess.run([find_command_path("isort"), source]).returncode  # noqa: S603 # Not checking inputs as they are passed almost directly to the command.
            returncode += subprocess.run([find_command_path("ruff"), "format", source]).returncode  # noqa: S603 # Not checking inputs as they are passed almost directly to the command.
        _LOGGER.info("Done formatting sources.")

        return returncode == 0
