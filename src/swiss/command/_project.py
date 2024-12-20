"""Project creation and manipulation tool."""

import logging
from argparse import ArgumentParser, Namespace, _SubParsersAction

import copier

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)
PROJECT_TEMPLATES = {
    "python": "http://192.168.1.27:10880/CrowsClub/python_template.git"
}


class ProjectCommand(BaseCommand):
    """Class containing project commands."""

    NAME = "project"
    DESCRIPTION = "Run project commands for ease of use."

    def __init__(self) -> None:
        """Constructor for ProjectCommand."""
        super().__init__(self.NAME, self.DESCRIPTION)

    def add_to_parser(self, root_parser: _SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
        docker_parser: ArgumentParser = root_parser.add_parser(
            self.name, help=self.description
        )
        docker_subparsers = docker_parser.add_subparsers(
            help="Project sub commands.", required=True
        )

        # ---------------------------------------------------------------------
        # Create a project from a project template.
        # ---------------------------------------------------------------------
        clean_parser = docker_subparsers.add_parser(
            "create", help="Create a project from a project template."
        )
        clean_parser.add_argument(
            "type",
            help=f"The project type. Choices: {list(PROJECT_TEMPLATES.keys())}.",
            choices=list(PROJECT_TEMPLATES.keys()),
        )
        clean_parser.add_argument(
            "destination", help="The destination directory for the new project."
        )
        clean_parser.set_defaults(func=self._handle_create)

    def _handle_create(self, args: Namespace) -> bool:
        """Handle the create sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        copier.run_copy(PROJECT_TEMPLATES[args.type], args.destination)

        return True
