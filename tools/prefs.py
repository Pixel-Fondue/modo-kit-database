from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Paths:
    """All paths related to building the database."""
    ROOT = Path(__file__).parent.parent.absolute()
    # Data paths
    QUERIES = ROOT / "queries"
    KITS_ROOT = ROOT / "kits"
    # Database
    DATABASE = ROOT / "mkc_kits.db"


@dataclass()
class DataKeys:
    """Dataclass to hold all database keys"""
    # Table keys
    table_kits = 'table_kits'
    table_authors = 'table_authors'
    insert_kit = 'insert_kit'
    insert_author = 'insert_author'
    # Generation keys
    vacuum = 'VACUUM'
    set_page_size = "PRAGMA page_size = 1024"
