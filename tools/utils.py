from typing import Dict

from .prefs import Paths


def load_queries() -> Dict[str, str]:
    """Loads all query files from SCRIPT_QUERIES.

    Returns:
        queries: A dictionary of query names and their contents.
    """
    return {query.stem: query.read_text() for query in Paths.QUERIES.glob("*.sql")}


def readable_size(size: int, decimal: int = 2) -> str:
    """Converts a byte size into a human-readable format.

    Args:
        size: The size in bytes.
        decimal: The number of decimal places to display.

    Returns:
        The size in a human-readable format.
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0:
            return f"{size:.{decimal}f} {unit}"
        size /= 1024.0

    return f"{size:.{decimal}f} {unit}"
