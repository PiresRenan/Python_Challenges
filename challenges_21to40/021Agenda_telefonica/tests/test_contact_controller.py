import unittest

from database import Database
from src.models.user import User
from src.models.contact import Contact
from src.controllers.user_controller import UserController
from src.controllers.contact_controller import ContactController


class MyTestCase(unittest.TestCase):
    def setUp(self):
        db = Database("", "", "")
        username = "testuser"
        password = "testpassword"
        self.user = User(username, password)

        self.user_controller = UserController(db)
        self.user_controller.create_users_table()
        try:
            self.user_controller.create_user(self.user.username, self.user.password)
        except Exception as e:
            raise Exception(e)

        self.contact_controller = ContactController(db)
        self.contact_controller.create_contacts_table()
        contact = Contact(self.user.username, "teste@teste.com", "11223344556")

        try:
            self.contact_controller.create_contact(1, username, contact.email, contact.phone_number)
        except Exception as e:
            raise Exception(e)

    def test_create_new_contact(self):
        email = "maisteste@teste.com"
        phone_number = "99887755443"
        print(self.user.username)
        # new_contact = Contact(self.user.username, email, phone_number)
        # self.assertIsInstance(new_contact, User)
        # self.assertEqual(new_contact.username, email)
        # self.assertEqual(new_contact.password, phone_number)


if __name__ == '__main__':
    unittest.main()
