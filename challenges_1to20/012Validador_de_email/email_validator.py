import re


class EmailValidator:
    def __init__(self):
        # Lista de domínios comuns de e-mail
        self.common_domains = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com"]

    def validate(self, email):
        # Expressão regular para validar o formato do e-mail
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Verifica se o e-mail corresponde ao padrão
        if re.match(pattern, email):
            # Extrai o domínio do e-mail
            domain = email.split('@')[1]
            # Verifica se o domínio está na lista de domínios comuns
            if domain in self.common_domains:
                return True
        return False
