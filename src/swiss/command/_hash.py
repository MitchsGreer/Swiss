"""Hash the files in the given directory."""

import hashlib
import logging
import shutil
from argparse import ArgumentParser, Namespace, _SubParsersAction
from pathlib import Path

from ._base import BaseCommand

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class HashCommand(BaseCommand):
    """Class for the hash command."""

    NAME = "hash"
    DESCRIPTION = "Hash the files in the given directory."

    def __init__(self: "HashCommand") -> None:
        """Constructor for HashCommand."""
        super().__init__(self.NAME, self.DESCRIPTION)

    def add_to_parser(self: "HashCommand", root_parser: _SubParsersAction) -> None:
        """Add parser arguments and subparsers for this command.

        Args:
            root_parser: The root parser to add too.
        """
        parser: ArgumentParser = root_parser.add_parser(self.name, help=self.description)
        parser.add_argument("dir", help="The directory to hash files of.", type=Path)
        parser.add_argument(
            "--rename",
            help="Flag to rename all files in this directory with their hashes.",
            action="store_true",
            default=False,
        )
        parser.add_argument(
            "--recurse",
            help="Recursively move through directories.",
            action="store_true",
            default=False,
        )
        parser.set_defaults(func=self._handle_hash)

    def _handle_hash(self: "HashCommand", args: Namespace) -> bool:
        """Hash all the files in the given directory.

        Args:
            args: The command line arguments.

        Returns:
            True if the command runs successfully, False otherwise.
        """
        success = True

        glob_pattern = "*"
        if args.recurse:
            glob_pattern = "**/*"

        target_files = [globbed_file for globbed_file in Path(args.dir).glob(glob_pattern) if globbed_file.is_file()]
        for target in target_files:
            digest = hashlib.md5(target.read_bytes()).hexdigest()  # noqa: S324 # Use of MD5 for hashing files for naming.

            _LOGGER.info(f"{target.absolute()}: {digest}")

            if args.rename:
                try:
                    _LOGGER.info(f"Renaming: {target} -> {target.with_name(digest).with_suffix(target.suffix)}")
                    shutil.move(target, target.with_name(digest).with_suffix(target.suffix))
                except PermissionError:
                    _LOGGER.error(
                        f"Could not rename: {target} -> {target.with_name(digest).with_suffix(target.suffix)}",
                    )
                    success = False

        return success
