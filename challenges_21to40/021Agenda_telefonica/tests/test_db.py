import unittest
from database import Database


class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        db = Database("", "", "")
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
