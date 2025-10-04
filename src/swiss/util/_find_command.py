"""Utility to find the given command."""

import shutil

from swiss.exceptions import CommandNotFoundError


def find_command_path(command: str) -> str:
    """Find the path to the command.

    Raises:
        CommandNotFoundError: If the command is not found.

    Args:
        command: The command to find the path for.

    Returns:
        The path to the command.
    """
    command_path = shutil.which(command)

    if command_path is None:
        raise CommandNotFoundError("Could not find command [%s], is it installed on the system?" % (command))

    return command_path
