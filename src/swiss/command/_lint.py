"""Lint the given source directories."""

import logging
import subprocess
from argparse import ArgumentParser, Namespace, _SubParsersAction

from swiss.util import find_command_path

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class LintCommand(BaseCommand):
    """Class for the lint command."""

    NAME = "lint"
    DESCRIPTION = "Lint the given source directories."

    def __init__(self: "LintCommand") -> None:
        """Constructor for LintCommand."""
        super().__init__(self.NAME, self.DESCRIPTION)

    def add_to_parser(self: "LintCommand", root_parser: _SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
        swing_parser: ArgumentParser = root_parser.add_parser(self.name, help=self.description)
        swing_parser.add_argument(
            "source",
            metavar="SOURCE",
            help="The python sources to lint.",
            nargs="+",
        )
        swing_parser.set_defaults(func=self._handle_lint)

    def _handle_lint(self: "LintCommand", args: Namespace) -> bool:
        """Handle the lint sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        returncode = 0

        _LOGGER.info("Linting sources.")
        for source in args.source:
            _LOGGER.info(f"\tLinting {source}.")
            returncode += subprocess.run(
                [  # noqa: S603 # Not checking inputs as they are passed almost directly to the command.
                    find_command_path("ruff"),
                    "check",
                    "--select",
                    "ERA,ANN,S,BLE,FBT,B,A,COM,C4,DTZ,T10,EM,FIX,FA,INT,ISC,ICN,LOG,INP,PIE,T20,PT,Q,RSE,RET,SLF,SIM,TID,TD,ARG,PTH,I,N,E,F,RUF",
                    source,
                ],
            ).returncode
        _LOGGER.info("Done Linting sources.")

        return returncode == 0
