import os
import unittest
from dotenv import load_dotenv

from database import Database

load_dotenv()


class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        dbname = os.getenv("DB_NAME")
        userdb = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        db = Database(dbname, userdb, password)
        db.connect()
        self.assertTrue(db.is_connected())
        db.close_db()

    def test_cursor(self):
        user_esperado = (1, 'teste', '123abc')
        db = Database("", "", "")
        db.connect()
        cursor = db.connection.cursor()
        cursor.execute('select * from users')
        user1 = cursor.fetchone()
        self.assertEqual(user1, user_esperado)


if __name__ == '__main__':
    unittest.main()
