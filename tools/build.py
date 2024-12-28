from pathlib import Path
from typing import Generator

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


if __name__ == '__main__':
    with MKCDatabase() as mkc_db:
        for kit_info in get_kits():
            mkc_db.load_kit(kit_info)
