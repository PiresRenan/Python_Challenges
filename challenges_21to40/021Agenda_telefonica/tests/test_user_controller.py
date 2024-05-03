import os
import unittest
from dotenv import load_dotenv

from database import Database
from src.controllers.user_controller import UserController
from src.models.user import User

load_dotenv()


class TestUserController(unittest.TestCase):
    def setUp(self):
        dbname = os.getenv("DB_NAME")
        userdb = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        db = Database(dbname, userdb, password)
        self.user = User("testuser", "testePassword")
        self.user_controller = UserController(db)
        self.user_controller.create_users_table()
        try:
            self.user_controller.create_user(self.user.username, self.user.password)
        except Exception as e:
            raise Exception(e)

    def tearDown(self):
        self.user_controller.drop_table()

    def test_create_user(self):
        user2 = User("teste2", "testdesenha")
        new_user = self.user_controller.create_user(user2.username, user2.password)

        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.username, user2.username)
        self.assertEqual(new_user.password, user2.password)

    def test_find_all(self):
        users = self.user_controller.find_all()
        self.assertIsNotNone(users)

    def test_find_user(self):
        founded_user = self.user_controller.find_user(self.user.username)
        self.assertEqual(founded_user.username, self.user.username)

    def test_update_password(self):
        password = "<PASSWORD>"
        self.assertTrue(self.user_controller.update_password(self.user.username, password))

    def test_delete_user(self):
        id = "1"
        self.assertTrue(self.user_controller.delete_user(id))


if __name__ == '__main__':
    unittest.main()
