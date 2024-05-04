from src.utils.validator import Validator


class Contact:
    def __init__(self, contact_id, username, email, phone_number):
        if not Validator.validate_username(username):
            raise ValueError("Nome de usuario inválido!")
        if not Validator.validate_email(email):
            raise ValueError("Email inválido!")
        if not Validator.validate_phone_number(phone_number):
            raise ValueError("Telefone inválido")
        self.contact_id = contact_id
        self.username = username
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"Contact ID: {self.contact_id}, Username: {self.username}, Email: {self.email}, Phone number: {self.phone_number}"