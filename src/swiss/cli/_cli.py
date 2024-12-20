"""The command line interface for this module."""

import argparse
import logging
import sys
from typing import List, Type

from swiss.command import (BaseCommand, CloneCommand, DockerCommand,
                           FormatCommand, ImportCommand,
                           InstallEditableCommand, LintCommand, ProjectCommand,
                           RemoveCommand, SwingCommand)
from swiss.exceptions import CommandNotFoundError, NotInVenvError

COMMANDS: List[Type[BaseCommand]] = [
    DockerCommand,
    SwingCommand,
    ImportCommand,
    RemoveCommand,
    InstallEditableCommand,
    FormatCommand,
    ProjectCommand,
    LintCommand,
    CloneCommand,
]
COMMANDS.sort(key=lambda x: x().name)

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class CLI:
    """Command line interface."""

    def __init__(self) -> None:
        """Constructor for CLI."""
        self.parser = argparse.ArgumentParser("swiss", "Command line swiss army knife.")
        subparsers = self.parser.add_subparsers(required=True)

        for command in COMMANDS:
            command().add_to_parser(subparsers)

    def run(self) -> bool:
        """Parse and run the command.

        Returns:
            True if the command was successful, False otherwise.
        """
        success = False
        command = " ".join(sys.argv)

        args = self.parser.parse_args()

        try:
            success = args.func(args)
        except NotInVenvError:
            _LOGGER.error(
                f"Could not run command [{command}] outside of a virtual environment."
            )
        except CommandNotFoundError as e:
            _LOGGER.error(f"Could not find command [{e.args[0]}].")

        if not success:
            _LOGGER.error(f"[{command}] failed to run.")

        return success
