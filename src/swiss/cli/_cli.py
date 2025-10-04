"""The command line interface for this module."""

from __future__ import annotations

import argparse
import logging
import sys
from typing import List, Type

from swiss.command import (
    BaseCommand,
    CloneCommand,
    DockerCommand,
    FormatCommand,
    HashCommand,
    ImportCommand,
    InstallEditableCommand,
    LintCommand,
    ProjectCommand,
    RemoveCommand,
    SpaceFindCommand,
    SwingCommand,
    VersionCommand,
)
from swiss.exceptions import CommandNotFoundError, InvalidCommandInputError, NotInVenvError

COMMANDS: List[Type[BaseCommand]] = [
    CloneCommand,
    DockerCommand,
    FormatCommand,
    HashCommand,
    ImportCommand,
    InstallEditableCommand,
    LintCommand,
    ProjectCommand,
    RemoveCommand,
    SpaceFindCommand,
    SwingCommand,
    VersionCommand,
]
COMMANDS.sort(key=lambda x: x().name)

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class CLI:
    """Command line interface."""

    def __init__(self: "CLI") -> None:
        """Construct a CLI object."""
        self.parser = argparse.ArgumentParser("swiss", "Command line swiss army knife.")
        subparsers = self.parser.add_subparsers(required=True)

        for command in COMMANDS:
            command().add_to_parser(subparsers)

    def run(self: "CLI") -> bool:
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
            _LOGGER.error(f"Could not run command [{command}] outside of a virtual environment.")
        except CommandNotFoundError as e:
            _LOGGER.error(e)
        except InvalidCommandInputError as e:
            _LOGGER.error(e)

        if not success:
            _LOGGER.error(f"[{command}] failed to run.")

        return success
