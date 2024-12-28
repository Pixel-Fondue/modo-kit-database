from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class Paths:
    """All paths related to building the database."""
    ROOT = Path(__file__).parent.parent.absolute()
    # Data paths
    QUERIES = ROOT / "queries"
    KITS_ROOT = ROOT / "kits"
    # Database
    BUILD = ROOT / "build"
    DATABASE = BUILD / "mkc_kits.db"
    MANIFEST = BUILD / "manifest.json"


@dataclass()
class DataKeys:
    """Dataclass to hold all database keys"""
    # Table keys
    table_kits = 'table_kits'
    table_authors = 'table_authors'
    insert_kit = 'insert_kit'
    insert_author = 'insert_author'
    # Database keys
    kits = 'kits'
    authors = 'authors'
    # Generation keys
    vacuum = 'VACUUM'
    set_page_size = "PRAGMA page_size = 1024"


@dataclass()
class QueryKey:
    """Dataclass to hold a database variable and required."""
    name: str
    type: Any
    required: bool = False

# Conversion map for query types
QueryTypeMap ={
    'TEXT': str,
    'INTEGER': int,
    'BOOLEAN': bool,
    'JSON': dict,
    'REAL': float
}
