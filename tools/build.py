import json
from pathlib import Path
from typing import Generator

from .utils import get_version
from .prefs import Paths
from .database import MKCDatabase


def get_kits() -> Generator[Path, None, None]:
    """Gathers all kits and builds the database.

    Yields:
        kit_file: The path to the kit.json file.
    """
    # Iterate over the kits directory for all kit.json files.
    for kit_file in Paths.KITS_ROOT.rglob("kit.json"):
        yield kit_file


def get_authors() -> Generator[Path, None, None]:
    """Gathers all authors and builds the database.

    Yields:
        author_file: The path to the info.json file.
    """
    # Iterate over the authors directory for all author.json files.
    for author_file in Paths.KITS_ROOT.rglob("info.json"):
        yield author_file


def build_database() -> None:
    """Builds the database for all kits in `kits.json`."""
    with MKCDatabase() as mkc_db:
        # Load all kits into the database.
        for kit_info in get_kits():
            mkc_db.load_kit(kit_info)
        # Load all authors into the database.
        for author_info in get_authors():
            mkc_db.load_author(author_info)


def build_manifest() -> None:
    """Builds the manifest.json file for the database file."""
    # Get the version of the project.
    version = get_version()
    # Create the manifest dictionary.
    manifest = {
        "version": version,
        "file": "mkc_kits.db"
    }
    # Write the manifest to the build directory.
    Paths.MANIFEST.write_text(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    build_database()
    build_manifest()
