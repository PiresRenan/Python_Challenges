import unittest

from database import Database
from src.controllers.user_controller import UserController
from src.models.user import User


class TestUserController(unittest.TestCase):
    def setUp(self):
        db = Database("", "", "")
        username = "testuser"
        password = "testpassword"
        self.user_controller = UserController(db)
        self.user_controller.create_users_table()
        try:
            self.user_controller.create_user(username, password)
        except Exception as e:
            raise Exception(e)

    def tearDown(self):
        self.user_controller.drop_table()

    def test_create_user(self):
        username = "teste2"
        password = "testdesenha"
        new_user = self.user_controller.create_user(username, password)

        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.username, username)
        self.assertEqual(new_user.password, password)

    def test_find_all(self):
        users = self.user_controller.find_all()
        self.assertIsNotNone(users)

    def test_find_user(self):
        username_esperado = "testuser"
        user = self.user_controller.find_user(username_esperado)
        self.assertEqual(user.username, username_esperado)

    def test_update_password(self):
        username = "testuser"
        password = "<PASSWORD>"
        self.assertTrue(self.user_controller.update_password(username, password))

    def test_delete_user(self):
        id = "1"
        self.assertTrue(self.user_controller.delete_user(id))


if __name__ == '__main__':
    unittest.main()
