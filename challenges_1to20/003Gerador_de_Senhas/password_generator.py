import random
import string


class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password
