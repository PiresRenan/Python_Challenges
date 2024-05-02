import re


class Validator:
    @staticmethod
    def validate_username(username):
        return len(username) >= 3

    @staticmethod
    def validate_password(password):
        return len(password) >= 6

    @staticmethod
    def validate_email(email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email)

    @staticmethod
    def validate_phone_number(phone_number):
        return len(phone_number) >= 7