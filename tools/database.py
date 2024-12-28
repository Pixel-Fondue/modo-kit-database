import json
from typing import Type
from pathlib import Path
from types import TracebackType
from sqlite3 import connect, Cursor, Connection

from .prefs import Paths, DataKeys as DKeys
from .utils import load_queries, get_table_names, get_table_insert, format_value_for_query


class MKCDatabase:
    """Class ot manage the generation of the mkc kit database.

    Attributes:
        cursor: The database cursor.
        connection: The database connection.
    """
    cursor: Cursor
    connection: Connection

    def __init__(self) -> None:
        """Initializes the database generator."""
        self.query = load_queries()
        self.kit_table_query = self.query.get(DKeys.table_kits)
        self.kit_table_names = get_table_names(self.kit_table_query)
        self.kit_insert_query = get_table_insert(DKeys.kits, self.kit_table_names)
        self.author_table_query = self.query.get(DKeys.table_authors)

    def __enter__(self) -> 'MKCDatabase':
        """Enters the context manager.

        Returns:
            self: This database manager.
        """
        self._init_database()
        return self

    def __exit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> bool:
        """Exits the context manager.

        Returns:
            False: Always returns False to raise any exceptions.
        """
        self.connection.commit()
        self.connection.close()
        return False

    def _init_database(self) -> None:
        """Initializes the mkc database for all kits and authors."""
        # Delete the database if it exists.
        if Paths.DATABASE.exists():
            Paths.DATABASE.unlink()

        # Connect to the database.
        self.connection = connect(Paths.DATABASE)
        # Initialize the database.
        self.cursor = self.connection.cursor()
        self.cursor.execute(DKeys.set_page_size)
        self.cursor.execute(DKeys.vacuum)
        # Create the table for the kits.
        self.cursor.execute(self.query.get(DKeys.table_kits))
        # Create the table for the authors.
        self.cursor.execute(self.query.get(DKeys.table_authors))

    def load_kit(self, kit_info: Path) -> None:
        """Loads in the kit.json file and populates the database.

        Args:
            kit_info: The path to the kits `kit.json` file.

        Raises:
            ValueError: If a required key is missing from the kit data.
        """
        # The SQL query to insert the kit data.
        kit_table_query = self.query.get(DKeys.table_kits)
        # The data to populate the kit table with.
        kit_data = json.loads(kit_info.read_text())
        # List to hold the values for the query in the correct order.
        query_values = []
        # Iterate over the table names and grab the values from the kit data.
        # This method will ensure the database is populated in the correct order.
        for query_key in get_table_names(kit_table_query):
            query_value = kit_data.get(query_key.name, None)
            if query_value is None and query_key.required:
                raise ValueError(f"Missing required key: {query_key.name}")
            else:
                formatted_value = format_value_for_query(query_value, query_key)
                query_values.append(formatted_value)

        # Insert the kit data into the database.
        self.cursor.execute(self.kit_insert_query, query_values)
