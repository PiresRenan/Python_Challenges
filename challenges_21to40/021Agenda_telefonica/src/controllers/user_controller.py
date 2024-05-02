import psycopg2
from ..models.user import User


class UserController:
    def __init__(self, db):
        self.db = db
        self.db.connect()

    def create_users_table(self):
        try:
            create_table_query = """
                        CREATE TABLE users (
                            id SERIAL PRIMARY KEY UNIQUE,
                            username VARCHAR(255) UNIQUE NOT NULL,
                            password VARCHAR(255) NOT NULL
                        );
                    """
            with self.db.connection.cursor() as cursor:
                cursor.execute(create_table_query)
                self.db.connection.commit()
                cursor.close()
        except psycopg2.Error as e:
            self.db.connection.rollback()
            print(e)

    def drop_table(self):
        try:
            drop_table_query = """
                        DROP TABLE IF EXISTS users;
                    """
            with self.db.connection.cursor() as cursor:
                cursor.execute(drop_table_query)
                self.db.connection.commit()
                cursor.close()
        except psycopg2.Error as e:
            self.db.connection.rollback()
            print(e)

    def create_user(self, username, password):
        try:
            cursor = self.db.connection.cursor()
            insert_query = """
                INSERT INTO users (username, password)
                VALUES (%s, %s)
                RETURNING id, username, password
            """

            cursor.execute(insert_query, (username, password))
            self.db.connection.commit()
            new_user_data = cursor.fetchone()
            new_user = User(new_user_data[1], new_user_data[2])
            cursor.close()
            return new_user
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e

    def find_all(self):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM users;")
            self.db.connection.commit()
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e

    def find_user(self, username):
        try:
            cursor = self.db.connection.cursor()
            select_query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(select_query, (username,))
            self.db.connection.commit()
            user_record = cursor.fetchone()
            founded_user = User(user_record[1], user_record[2])
            cursor.close()
            return founded_user
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e

    def update_password(self, usename, new_password):
        try:
            cursor = self.db.connection.cursor()
            update_query = "UPDATE users SET password = %s WHERE username = %s"
            cursor.execute(update_query, (new_password, usename))
            self.db.connection.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e

    def delete_user(self, id:str):
        try:
            cursor = self.db.connection.cursor()
            delete_query = "DELETE FROM users WHERE id = %s"
            cursor.execute(delete_query, id)
            self.db.connection.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            self.db.connection.rollback()
            raise e

