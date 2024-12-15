from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Paths:
    """All paths related to building the database."""
    ROOT = Path(__file__).parent.parent.absolute()
    # Data paths
    QUERIES = ROOT / "queries"
    KITS_ROOT = ROOT / "kits"
