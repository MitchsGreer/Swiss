"""Find the files with spaces in the given directory."""

import logging
import shutil
from argparse import ArgumentParser, Namespace, _SubParsersAction
from pathlib import Path

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class SpaceFindCommand(BaseCommand):
    """Class for the space find command."""

    NAME = "space-find"
    DESCRIPTION = "Find the files with spaces in the given directory."

    def __init__(self) -> None:
        """Constructor for SpaceFindCommand."""
        super().__init__(self.NAME, self.DESCRIPTION)

    def add_to_parser(self, root_parser: _SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
        space_find_parser: ArgumentParser = root_parser.add_parser(
            self.name, help=self.description
        )
        space_find_parser.add_argument(
            "dir", help="The directory to hash files of.", type=Path
        )
        space_find_parser.add_argument(
            "--rename",
            help="Flag to rename all files in this directory without spaces.",
            action="store_true",
            default=False,
        )
        space_find_parser.add_argument(
            "--recurse",
            help="Recursively move through directories.",
            action="store_true",
            default=False,
        )

        space_find_parser.set_defaults(func=self._handle_hash)

    def _handle_hash(self, args: Namespace) -> bool:
        """Find the files with spaces in the given directory.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        success = True
        root = Path(args.dir).resolve()

        glob_pattern = "*"
        if args.recurse:
            glob_pattern = "**/*"

        target_files = [
            globbed_file.resolve()
            for globbed_file in root.glob(glob_pattern)
            if " " in globbed_file.name and globbed_file.is_file()
        ]

        target_directories = [
            globbed_file.resolve()
            for globbed_file in root.glob(glob_pattern)
            if " " in globbed_file.name and globbed_file.is_dir()
        ]
        target_directories.sort(key=lambda d: len(d.parents))

        for target in target_directories:
            _LOGGER.info(f"{target.absolute()}")

            if args.rename:
                ending_dir = Path(
                    root, str(target).replace(str(root), "")[1:].replace(" ", "_")
                )
                starting_dir = Path(ending_dir.parent, target.name)

                _LOGGER.info(f"Renaming: {starting_dir} -> {ending_dir}")
                try:
                    shutil.move(starting_dir, ending_dir)
                except PermissionError:
                    _LOGGER.error(f"Could not rename: {starting_dir} -> {ending_dir}")
                    success = False

        for target in target_files:
            _LOGGER.info(f"{target.absolute()}")

            if args.rename:
                ending_file = Path(
                    root, str(target).replace(str(root), "")[1:].replace(" ", "_")
                )
                starting_file = Path(ending_file.parent, target.name)

                _LOGGER.info(f"Renaming: {starting_file} -> {ending_file}")
                try:
                    shutil.move(starting_file, ending_file)
                except PermissionError:
                    _LOGGER.error(f"Could not rename: {starting_file} -> {ending_file}")
                    success = False

        return success
