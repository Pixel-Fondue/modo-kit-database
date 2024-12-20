from sqlite3 import connect

from .prefs import Paths, DataKeys as DKeys
from .utils import load_queries


class MKCDatabase:
    """Class ot manage the generation of the mkc kit databse."""

    def __init__(self):
        self.query = load_queries()

    def build_database(self) -> None:
        """Builds the database for all kits in `kits.json`."""
        # Delete the database if it exists.
        if Paths.DATABASE.exists():
            Paths.DATABASE.unlink()

        # Create database with the kits' data.
        with connect(Paths.DATABASE) as connection:
            # Initialize the database.
            cursor = connection.cursor()
            cursor.execute(DKeys.set_page_size)
            cursor.execute(DKeys.vacuum)
            # Create the table for the kits.
            cursor.execute(self.query.get(DKeys.table_kits))
            # Create the table for the authors.
            cursor.execute(self.query.get(DKeys.table_authors))


if __name__ == "__main__":
    MKCDatabase().build_database()