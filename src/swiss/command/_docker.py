"""Run docker commands for ease of use."""

# ruff: noqa: S603

import logging
import subprocess
from argparse import ArgumentParser, Namespace, _SubParsersAction

from swiss.util import find_command_path

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class DockerCommand(BaseCommand):
    """Class containing docker commands."""

    NAME = "docker"
    DESCRIPTION = "Run docker commands for ease of use."

    def __init__(self: "DockerCommand") -> None:
        """Constructor for DockerCommand."""
        super().__init__(self.NAME, self.DESCRIPTION)

    def add_to_parser(self: "DockerCommand", root_parser: _SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
        docker_parser: ArgumentParser = root_parser.add_parser(self.name, help=self.description)
        docker_subparsers = docker_parser.add_subparsers(help="Docker sub commands.", required=True)

        # ---------------------------------------------------------------------
        # Clean up docker structures.
        # ---------------------------------------------------------------------
        clean_parser = docker_subparsers.add_parser("clean", help="Clean up docker structures.")
        clean_parser.add_argument(
            "--stop",
            "-s",
            help="Stop all containers while pruning.",
            action="store_true",
            default=False,
        )
        clean_parser.add_argument(
            "--volumes",
            "-v",
            help="Prune docker volumes.",
            action="store_true",
            default=False,
        )
        clean_parser.add_argument(
            "--networks",
            "-n",
            help="Prune docker networks.",
            action="store_true",
            default=False,
        )
        clean_parser.add_argument(
            "--images",
            "-i",
            help="Prune docker images.",
            action="store_true",
            default=False,
        )
        clean_parser.add_argument(
            "--containers",
            "-c",
            help="Prune docker containers.",
            action="store_true",
            default=False,
        )
        clean_parser.add_argument(
            "--all",
            "-a",
            help="Prune all docker structures we can.",
            action="store_true",
            default=False,
        )
        clean_parser.set_defaults(func=self._handle_clean)

        # ---------------------------------------------------------------------
        # Stop all docker containers.
        # ---------------------------------------------------------------------
        stop_parser = docker_subparsers.add_parser("stop", help="Stop all docker containers.")
        stop_parser.set_defaults(func=self._handle_stop)

    def _handle_clean(self: "DockerCommand", args: Namespace) -> bool:
        """Handle the clean sub command.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        returncode = 0
        success = True

        if args.stop:
            success = self._handle_stop(args)

        if success and (args.containers or args.all):
            _LOGGER.info("Pruning containers...")
            returncode += subprocess.run([find_command_path("docker"), "container", "prune", "-f"]).returncode
            _LOGGER.info("Containers pruned.")

        if success and (args.images or args.all):
            _LOGGER.info("Pruning images...")
            returncode += subprocess.run([find_command_path("docker"), "image", "prune", "-a", "-f"]).returncode
            _LOGGER.info("Images pruned.")

        if success and (args.volumes or args.all):
            _LOGGER.info("Pruning volumes...")
            returncode = subprocess.run([find_command_path("docker"), "volume", "prune", "-a", "-f"]).returncode
            _LOGGER.info("Volumes pruned.")

        if success and (args.networks or args.all):
            _LOGGER.info("Pruning networks...")
            returncode += subprocess.run([find_command_path("docker"), "network", "prune", "-f"]).returncode
            _LOGGER.info("Networks pruned.")

        return success and returncode == 0

    def _handle_stop(self: "DockerCommand", _: Namespace) -> bool:
        """Handle the stop sub command.

        Args:
            _: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        _LOGGER.info("Stopping all docker containers...")

        success = False
        process = subprocess.run([find_command_path("docker"), "container", "ls", "-q"], capture_output=True)
        success = process.returncode == 0

        if success:
            container_ids = process.stdout.decode(encoding="UTF-8").split("\n")
            container_ids = [ids for ids in container_ids if ids]
            _LOGGER.info(f"Stopping {container_ids}")

            if container_ids:
                command = [
                    find_command_path("docker"),
                    "container",
                    "stop",
                ]
                command.extend(container_ids)
                process = subprocess.run(command)
                success = process.returncode == 0

        _LOGGER.info("Stopped docker containers.")

        return success
