import sqlite3
from config import DATABASE_FILE_PATH


class DataBase:
    def __init__(self):
        self.connection = self.create_database()
        try:
            self.create_table()
        except sqlite3.OperationalError:
            pass

    def store_result(self, result: int):
        self.connection.execute(
            """
            INSERT INTO GameRuns (level) VALUES (?)
            """,
            [result]
        )

    def query_highscore(self):
        return self.connection.execute(
            """
            SELECT MAX(level)
            FROM GameRuns
            """
        ).fetchone()[0]

    def query_number_of_runs(self):
        return self.connection.execute(
            """
            SELECT COUNT(DISTINCT(id))
            FROM GameRuns
            """
        ).fetchone()[0]

    def create_database(self):
        connection = sqlite3.connect(DATABASE_FILE_PATH)
        connection.isolation_level = None
        return connection

    def create_table(self):

        self.connection.execute(
            """
            CREATE TABLE GameRuns (
                id INTEGER PRIMARY KEY,
                level INTEGER
            );
            """
        )


if __name__ == "__main__":
    db = DataBase()
    db.store_result(4)
    db.store_result(3)
    db.store_result(1)
    print(db.query_highscore())
    print(db.query_number_of_runs())
