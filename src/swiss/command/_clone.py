"""Clones down the given repository, if a directory is given, it checks out that branch."""

# ruff: noqa: S603

import logging
import subprocess
from argparse import ArgumentParser, Namespace, _SubParsersAction

from swiss.util import find_command_path

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class CloneCommand(BaseCommand):
    """Class for the clone command."""

    NAME = "clone"
    DESCRIPTION = "Clones down the given repository, if a directory is given, it checks out that branch."

    def __init__(self: "CloneCommand") -> None:
        """Constructor for CloneCommand."""
        super().__init__(self.NAME, self.DESCRIPTION)

    def add_to_parser(self: "CloneCommand", root_parser: _SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
        parser: ArgumentParser = root_parser.add_parser(
            self.name,
            help=self.description,
        )
        parser.add_argument(
            "url",
            metavar="URL",
            help="The URL for the git repository to clone.",
        )
        parser.add_argument(
            "--destination",
            "-d",
            metavar="DESTINATION",
            help="The destination directory and branch to checkout in the git repository.",
        )
        parser.set_defaults(func=self._handle_clone)

    def _handle_clone(self: "CloneCommand", args: Namespace) -> bool:
        """Handle the import sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        git_command = find_command_path("git")

        command = [git_command, "clone", args.url]
        if args.destination is not None:
            # Make a directory with the last segment of the repo branch path.
            # Ex: name/branch -> branch
            dest = args.destination.split("/")[-1]
            dest = dest.split("\\")[-1]

            _LOGGER.info(f"Cloning '{args.url}' into './{dest}'.")
            command.append(f"./{dest}")

        returncode = subprocess.run(command).returncode
        _LOGGER.info(f"Cloned '{args.url}'.")

        if returncode == 0 and args.destination is not None:
            _LOGGER.info(f"Switching to branch '{args.destination}'.")
            returncode = subprocess.run([git_command, "switch", dest], cwd=f"./{dest}").returncode
            _LOGGER.info(f"Switched to branch '{args.destination}'.")

        return returncode == 0
