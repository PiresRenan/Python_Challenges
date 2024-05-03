import psycopg2

from ..models.contact import Contact


class ContactController:
    def __init__(self, db):
        self.db = db
        self.db.connect()

    def create_contacts_table(self):
        try:
            create_table_query = """
                CREATE TABLE contacts (
                    id SERIAL PRIMARY KEY UNIQUE,
                    user_id INTEGER REFERENCES users(id),
                    username VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    phone_number VARCHAR(20) NOT NULL
                );
            """
            with self.db.connection.cursor() as cursor:
                cursor.execute(create_table_query)
                self.db.connection.commit()
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e

    def drop_table(self):
        try:
            drop_table_query = """
                DROP TABLE IF EXISTS contacts;
            """
            with self.db.connection.cursor() as cursor:
                cursor.execute(drop_table_query)
                self.db.connection.commit()
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e

    def create_contact(self, user_id, username, email, phone_number):
        try:
            cursor = self.db.connection.cursor()
            insert_query = """
                INSERT INTO contacts (user_id, username, email, phone_number)
                VALUES (%s, %s, %s, %s)
                RETURNING id, user_id, username, email, phone_number
            """

            cursor.execute(insert_query, (user_id, username, email, phone_number))
            self.db.connection.commit()
            new_contact_data = cursor.fetchone()
            new_contact = Contact(new_contact_data[2], new_contact_data[3], new_contact_data[4])
            return new_contact
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e

    def find_all_contacts(self, user_id):
        try:
            cursor = self.db.connection.cursor()
            select_query = "SELECT * FROM contacts WHERE user_id = %s"
            cursor.execute(select_query, (user_id,))
            self.db.connection.commit()
            contacts = cursor.fetchall()
            return contacts
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e

    def delete_contact(self, contact_id):
        try:
            cursor = self.db.connection.cursor()
            delete_query = "DELETE FROM contacts WHERE id = %s"
            cursor.execute(delete_query, (contact_id,))
            self.db.connection.commit()
            return True
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e