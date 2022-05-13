import sqlite3
from config import DATABASE_FILEPATH


class DataBase:
    """A class for providing database functionalities to the game and ui

    Attributes:
        custom_filepath: an optional attribute that allows for creating and
        using a data base in a different location than the default one. This
        allows for testing the DataBase class without the tests interfering
        with the user's actual gameplay data.

        connection: The connection to the database. This allows executing
        SQL on the database.
    """

    def __init__(self):
        """Inits DataBase"""

        self.connection = self.create_database()
        try:
            self.create_table()
        except sqlite3.OperationalError:
            pass

    def create_database(self):
        """Creates the database and sets up a connection to it.

        Returns:
            The connection to the database
        """

        connection = sqlite3.connect(DATABASE_FILEPATH)
        connection.isolation_level = None
        return connection

    def create_table(self):
        """Creates a table for storing data about game runs"""

        self.connection.execute(
            """
            CREATE TABLE GameRuns (
                id INTEGER PRIMARY KEY,
                level INTEGER
            );
            """
        )

    def store_result(self, result: int):
        """Stores a numeric result to the database

        Args:
            result: the highest level the player beats during a single game run
        """

        self.connection.execute(
            """
            INSERT INTO GameRuns (level) VALUES (?)
            """,
            [result]
        )

    def query_highscore(self):
        """Queries the database for the highest result

        Returns:
            The highest value in the level field of the GameRuns table
        """

        return self.connection.execute(
            """
            SELECT MAX(level)
            FROM GameRuns
            """
        ).fetchone()[0]

    def query_number_of_runs(self):
        """Queries the database for the total number of game runs

        Returns:
            The count of rows in the GameRuns table
        """

        return self.connection.execute(
            """
            SELECT COUNT(DISTINCT(id))
            FROM GameRuns
            """
        ).fetchone()[0]
