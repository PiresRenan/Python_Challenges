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
        self.contact_controller = ContactController(db)

        # Create Tables and users for tests
        self.user_controller.create_users_table()
        try:
            self.user_controller.create_user(self.user.username, self.user.password)
        except Exception as e:
            raise Exception(e)
        self.contact_controller.create_contacts_table()
        contact = Contact("1", self.user.username, "teste@teste.com", "11223344556")
        try:
            self.contact_controller.create_contact(1, username, contact.email, contact.phone_number)
        except Exception as e:
            raise Exception(e)

    def tearDown(self):
        self.contact_controller.drop_table()
        self.user_controller.drop_table()

    def test_create_new_contact(self):
        email = "maisteste@teste.com"
        phone_number = "99887755443"
        new_contact = Contact("0", self.user.username, email, phone_number)
        created_contact = self.contact_controller.create_contact("1", new_contact.username, new_contact.email,
                                                                 new_contact.phone_number)
        self.assertEqual(created_contact.email, email)
        self.assertEqual(created_contact.phone_number, phone_number)

    def test_find_all_contacts(self):
        contacts = self.contact_controller.find_all_contacts("1")
        self.assertIsNotNone(contacts)

    def test_find_contact_by_email(self):
        contacts = self.contact_controller.find_contact_by_email("1", "maisteste@teste.com")
        for contact in contacts:
            print(contact)
            self.assertEqual(contact.username, self.user.username)
            self.assertEqual(contact.email, "maisteste@teste.com")
            self.assertEqual(contact.phone_number, "99887755443")

    def test_update_contact(self):
        contacts = self.contact_controller.find_contact_by_email("1", "maisteste@teste.com")
        # update email
        for contact in contacts:
            self.assertTrue(self.contact_controller.update_contact("1", contact.contact_id,
                                                                   new_email="teste_update@email.com"))
        # update phone number
        for contact in contacts:
            self.assertTrue(self.contact_controller.update_contact("1", contact.contact_id,
                                                                   new_phone_number="12345678911"))

    def test_delete_contact(self):
        contacts = self.contact_controller.find_all_contacts("1")
        for contact in contacts:
            self.assertTrue(self.contact_controller.delete_contact(contact.contact_id))


if __name__ == '__main__':
    unittest.main()
