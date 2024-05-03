import os
import unittest
from dotenv import load_dotenv

from database import Database
from src.models.user import User
from src.models.contact import Contact
from src.controllers.user_controller import UserController
from src.controllers.contact_controller import ContactController

load_dotenv()


class MyTestCase(unittest.TestCase):
    def setUp(self):
        dbname = os.getenv("DB_NAME")
        userdb = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        db = Database(dbname, userdb, password)
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
        new_contact = Contact(self.user.username, email, phone_number)
        created_contact = self.contact_controller.create_contact("1", new_contact.username, new_contact.email, new_contact.phone_number)
        self.assertEqual(created_contact.email, email)
        self.assertEqual(created_contact.phone_number, phone_number)


if __name__ == '__main__':
    unittest.main()
