import unittest
import os
import sqlite3
from database import DataBase


DIRNAME = os.path.dirname(__file__)
TEST_DATABASE_FILE_PATH = os.path.join(
    DIRNAME,
    '..',
    '..',
    "data",
    "test_database.db"
)


class TestDataBase(unittest.TestCase):
    def setUp(self):
        # Start with a clean database
        try:
            os.remove(TEST_DATABASE_FILE_PATH)
        except Exception:
            pass
        self.database = DataBase(custom_filepath=TEST_DATABASE_FILE_PATH)

    def test_store_result(self):
        self.database.store_result(1)
        count = self.database.connection.execute(
            """
            SELECT COUNT(*) FROM GameRuns
            """
        ).fetchone()[0]
        self.assertEqual(count, 1)

    def test_query_highscore(self):
        self.database.store_result(1)
        self.database.store_result(3)
        self.database.store_result(2)
        highscore = self.database.query_highscore()
        self.assertEqual(highscore, 3)

    def test_query_number_of_runs(self):
        self.database.store_result(1)
        self.database.store_result(3)
        count = self.database.query_number_of_runs()
        self.assertEqual(count, 2)


# db.store_result(4)
# db.store_result(3)
# db.store_result(1)
# print(db.query_highscore())
# print(db.query_number_of_runs())
