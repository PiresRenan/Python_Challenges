from src.utils.validator import Validator


class User:
    def __init__(self, username, password):
        if not Validator.validate_username(username):
            raise ValueError("Nome de usuario inválido.")
        if not Validator.validate_password(password):
            raise ValueError("Senha inválida.")
        self.username = username
        self.password = password

    def __str__(self):
        return f'Username: {self.username}'
