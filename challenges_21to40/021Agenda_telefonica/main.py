from dotenv import load_dotenv
import os
from database import Database
from src.controllers.user_controller import UserController
from src.controllers.contact_controller import ContactController
from src.views.commandlineview import CommandLineView


def main():
    load_dotenv()

    dbname = os.getenv("DB_NAME")
    userdb = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db = Database(dbname, userdb, password)

    user_controller = UserController(db)
    try:
        user_controller.create_users_table()
    except Exception as e:
        pass
    contact_controller = ContactController(db)
    try:
        contact_controller.create_contacts_table()
    except Exception as e:
        pass

    cli_view = CommandLineView(user_controller, contact_controller)

    cli_view.main_menu()


if __name__ == "__main__":
    main()
