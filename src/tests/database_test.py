import unittest
from database import DataBase


class TestDataBase(unittest.TestCase):
    def setUp(self):
        # Start with a clean database
        self.database = DataBase()
        self.database.reset_database()

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

    def test_reset_database(self):
        self.database.store_result(1)
        self.database.reset_database()
        count = self.database.query_number_of_runs()
        self.assertEqual(count, 0)
