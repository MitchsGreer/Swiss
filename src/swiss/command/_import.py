"""Installs the given python modules into the the virtual environment we are in."""

import logging
import subprocess
import sys
from argparse import ArgumentParser, Namespace, _SubParsersAction

from swiss.util import in_venv

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class ImportCommand(BaseCommand):
    """Class for the import command."""

    NAME = "import"
    DESCRIPTION = "Install a python package in the virtual environment, don't install anything if we are not in one."

    def __init__(self) -> None:
        """Constructor for ImportCommand."""
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
            help="The python packages to install.",
            nargs="+",
        )
        swing_parser.set_defaults(func=self._handle_import)

    def _handle_import(self, args: Namespace) -> bool:
        """Handle the import sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        returncode = 0
        in_venv()

        _LOGGER.info("Installing packages into virtual environment.")
        for package in args.packages:
            _LOGGER.info(f"\tInstalling {package}.")
            returncode += subprocess.run(
                [sys.executable, "-m", "pip", "install", package]
            ).returncode
        _LOGGER.info("Done installing packages.")

        return returncode == 0
