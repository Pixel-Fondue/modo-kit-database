import json
from typing import Dict, List, Any

from .prefs import Paths, QueryKey, QueryTypeMap


def load_queries() -> Dict[str, str]:
    """Loads all query files from SCRIPT_QUERIES.

    Returns:
        queries: A dictionary of query names and their contents.
    """
    return {query.stem: query.read_text() for query in Paths.QUERIES.glob("*.sql")}


def format_value_for_query(value: Any, key: QueryKey) -> Any:
    """Formats a value to match the query type.

    Notes:
        This formatting is required to properly load JSON serialized data into an SQLite database.

    Args:
        value: The value to format.
        key: The key to format the value for.
    """
    if isinstance(value, bool):
        # SQLite uses 0 and 1 for boolean values.
        return 1 if value else 0
    elif isinstance(value, list) and key.type == str:
        # SQLite cannot store arrays, save as JSON string.
        return json.dumps(value)
    elif isinstance(value, key.type):
        # If the value is the correct type, return it.
        return value
    else:
        raise ValueError(f"Value {value} is not supported by the MKC database.")


def get_table_names(query: str) -> List[QueryKey]:
    """Extracts the query names from a query string.

    Args:
        query: The query string to extract names from.

    Returns:
        A list of query names.
    """
    names = []
    for line in query.splitlines():
        # Skip comments
        if line.startswith("--"):
            continue
        # If there are spaces, the first word is the query name.
        elif line.startswith("  "):
            # Get the first word as the key name and the second word as the key type.
            # Example: `    name TEXT NOT NULL,`
            key_name, key_type_name = line.split()[0:2]
            if key_name == "id":
                # Skip the id column
                continue
            else:
                # Check if NOT NULL is present
                required = True if "NOT NULL" in line else False
                key_type = QueryTypeMap.get(key_type_name, str)
                names.append(QueryKey(name=key_name, type=key_type, required=required))

    return names


def get_table_insert(table: str, keys: List[QueryKey]) -> str:
    """Generates an insert query for a table.

    Args:
        table: The table name.
        keys: The keys to insert into the table.

    Example:
        For each key, a ? is added as a placeholder for the value.
        `INSERT INTO table (key1, key2, key3) VALUES (?, ?, ?)`

    Returns:
        The formatted insert query.
    """
    column_names = ', '.join(key.name for key in keys)
    value_placeholders = ', '.join(['?' for _ in keys])
    return f"INSERT INTO {table} ({column_names}) VALUES ({value_placeholders})"


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
