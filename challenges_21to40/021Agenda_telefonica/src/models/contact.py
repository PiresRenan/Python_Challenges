from src.utils.validator import Validator


class Contact:
    def __init__(self, username, email, phone_number):
        if not Validator.validate_username(username):
            raise ValueError("Nome de usuario inválido!")
        if not Validator.validate_email(email):
            raise ValueError("Email inválido!")
        if not Validator.validate_phone_number(phone_number):
            raise ValueError("Telefone inválido")

        self.username = username
        self.email = email
        self.phone_number = phone_number
