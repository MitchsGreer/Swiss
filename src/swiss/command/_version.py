"""Format the given source directory."""

import logging
from argparse import ArgumentParser, Namespace, _SubParsersAction
from importlib.metadata import version

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class VersionCommand(BaseCommand):
    """Class for the format command."""

    NAME = "version"
    DESCRIPTION = "Display the version information for this tool."

    def __init__(self: "VersionCommand") -> None:
        """Constructor for FormatCommand."""
        super().__init__(self.NAME, self.DESCRIPTION)

    def add_to_parser(self: "VersionCommand", root_parser: _SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
        parser: ArgumentParser = root_parser.add_parser(self.name, help=self.description)
        parser.set_defaults(func=self._handle_version)

    def _handle_version(self: "VersionCommand", _: Namespace) -> bool:
        """Handle the format sub command.

        Args:
            _: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        _LOGGER.info(f"Swiss version: {version('swiss')}")

        return True
