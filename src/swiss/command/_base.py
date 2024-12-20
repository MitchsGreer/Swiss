"""Base command for swiss commands."""

import argparse
from abc import ABC, abstractmethod


class BaseCommand(ABC):

    def __init__(self, name: str, description: str) -> None:
        """Constructor for the base command.

        Args:
            name: The name of the command.
            description: What this command does.
        """
        self.name = name
        self.description = description

    @abstractmethod
    def add_to_parser(self, root_parser: argparse._SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
