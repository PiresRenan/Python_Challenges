from ..models.contact import Contact
from ..utils.validator import Validator

class ContactController:
    def add_contact(self, username, email, phone_number):
        if not Validator.validate_username(username):
            raise ValueError("Nome inválido.")
        if not Validator.validate_email(email):
            raise ValueError("Sobrenome inválido.")
        if not Validator.validate_phone_number(phone_number):
            raise ValueError("Número de telefone inválido.")

        # Adicionar um novo contato no banco de dados
        # (Implementação a ser feita posteriormente)

    def edit_contact(self, contact_id, first_name, last_name, phone_number):
        # Editar um contato existente no banco de dados
        # (Implementação a ser feita posteriormente)

    def delete_contact(self, contact_id):
        # Excluir um contato existente no banco de dados
        # (Implementação a ser feita posteriormente)

    def get_contacts(self, user_id):
        # Buscar contatos pertencentes a um usuário no banco de dados
        # (Implementação a ser feita posteriormente)