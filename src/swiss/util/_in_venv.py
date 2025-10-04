"""Utility to check if we are in a virtual environment."""

import sys

from swiss.exceptions import NotInVenvError


def in_venv() -> bool:
    """Check if we are in a virtual environment.

    Returns:
        True if we are in a venv False otherwise.
    """

    if sys.prefix == sys.base_prefix:
        raise NotInVenvError

    return True
