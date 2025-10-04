"""Get the branch this git repository is on."""

import subprocess

from ._find_command import find_command_path


def git_branch() -> str:
    """Get the branch this git repository is on.

    Returns:
        The name of the branch we are on.
    """
    return (
        subprocess.run(
            [find_command_path("git"), "rev-parse", "--abbrev-ref", "HEAD"],  # noqa: S603 # Not checking inputs as they are passed almost directly to the command.
            capture_output=True,
        )
        .stdout.decode("UTF-8")
        .replace("\n", "")
    )
