"""Remove the given python modules from the environment."""

import logging
import subprocess
import sys
from argparse import ArgumentParser, Namespace, _SubParsersAction

from swiss.util import in_venv

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class RemoveCommand(BaseCommand):
    """Class for the remove command."""

    NAME = "remove"
    DESCRIPTION = "Remove the given python modules from the environment."

    def __init__(self) -> None:
        """Constructor for RemoveCommand."""
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
            "packages",
            metavar="PACKAGES",
            help="The python packages to remove.",
            nargs="+",
        )
        swing_parser.set_defaults(func=self._handle_remove)

    def _handle_remove(self, args: Namespace) -> bool:
        """Handle the remove sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        returncode = 0
        in_venv()

        _LOGGER.info("Removing packages from virtual environment.")
        for package in args.packages:
            _LOGGER.info(f"\tRemoving {package}.")
            returncode += subprocess.run(
                [sys.executable, "-m", "pip", "uninstall", "-y", package]
            ).returncode
        _LOGGER.info("Done removing packages.")

        return returncode == 0
