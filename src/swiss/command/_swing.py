"""Swiss swing, does a `git add .`, `git commit -m ""`, 'git push origin <BRANCH>'."""

import logging
import subprocess
from argparse import ArgumentParser, Namespace, _SubParsersAction

from swiss.util import find_command_path, git_branch

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class SwingCommand(BaseCommand):
    """Class containing tarzan."""

    NAME = "swing"
    DESCRIPTION = "Does a `git add .`, `git commit -m " "`, 'git push origin <BRANCH>'"

    def __init__(self) -> None:
        """Constructor for DockerCommand."""
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
            "message",
            metavar="MESSAGE",
            help="The commit message to use when swinging in the format: swiss swing this is the commit message.",
            nargs="+",
        )
        swing_parser.set_defaults(func=self._handle_swing)

    def _handle_swing(self, args: Namespace) -> bool:
        """Handle the swing sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        returncode = 0

        _LOGGER.info("Swinging from tree to tree...")
        _LOGGER.info("\tAdding all files to stage.")
        returncode += subprocess.run(
            [
                find_command_path("git"),
                "add",
                ".",
            ]
        ).returncode

        if returncode == 0:
            _LOGGER.info("\tCommitting files with our message.")
            returncode += subprocess.run(
                [find_command_path("git"), "commit", "-m", " ".join(args.message)]
            ).returncode

        if returncode == 0:
            _LOGGER.info("\tPushing files up to the remote.")
            returncode += subprocess.run(
                [find_command_path("git"), "push", "origin", git_branch()]
            ).returncode

        _LOGGER.info("Tarzan is off the tree.")

        return returncode == 0
