class CommandLineView:
    def __init__(self, user_controller, contact_controller):
        self.user_controller = user_controller
        self.contact_controller = contact_controller
        self.current_user = None

    def create_or_login_user(self):
        while True:
            print("\nCriar novo usuário ou fazer login")
            choice = input("Digite '1' para criar um novo usuário, '2' para fazer login: ")

            if choice == "1":
                username = input("Nome de usuário: ")
                password = input("Senha: ")
                try:
                    self.user_controller.create_user(username, password)
                    print("Usuário criado com sucesso!")
                except Exception as e:
                    print(f"Erro ao criar o usuário: {e}")
            elif choice == "2":
                username = input("Nome de usuário: ")
                password = input("Senha: ")
                try:
                    user = self.user_controller.find_user(username)
                    if user and user.password == password:
                        print(f"Bem-vindo de volta, {username}!")
                        self.current_user = user
                        break
                    else:
                        print("Usuário ou senha incorretos. Tente novamente.")
                except Exception as e:
                    print(f"Erro ao fazer login: {e}")
            else:
                print("Opção inválida. Por favor, escolha novamente.")

    def main_menu(self):
        self.create_or_login_user()
        if not self.current_user:
            print("Acesso negado. Por favor, faça login.")
            return
        while True:
            print("\nAgenda Telefônica - Menu Principal")
            print("1. Criar novo contato")
            print("2. Buscar todos os contatos")
            print("3. Buscar contato por email")
            print("4. Atualizar contato")
            print("5. Excluir contato")
            print("6. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.create_contact()
            elif choice == "2":
                self.find_all_contacts()
            elif choice == "3":
                self.find_contact_by_email()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")

    def create_contact(self):
        print("\nCriar Novo Contato")
        user_id = input("ID do usuário: ")
        username = input("Nome do usuário: ")
        email = input("E-mail do contato: ")
        phone_number = input("Número de telefone do contato: ")

        try:
            new_contact = self.contact_controller.create_contact(user_id, username, email, phone_number)
            print("Novo contato criado com sucesso!")
            print(new_contact)
        except Exception as e:
            print(f"Erro ao criar o contato: {e}")

    def find_all_contacts(self):
        print("\nBuscar Todos os Contatos")
        user_id = input("ID do usuário: ")

        try:
            contacts = self.contact_controller.find_all_contacts(user_id)
            if contacts:
                print("Contatos encontrados:")
                for contact in contacts:
                    print(contact)
            else:
                print("Nenhum contato encontrado.")
        except Exception as e:
            print(f"Erro ao buscar contatos: {e}")

    def find_contact_by_email(self):
        print("\nBuscar Contato por Email")
        user_id = input("ID do usuário: ")
        email = input("E-mail do contato: ")

        try:
            contacts = self.contact_controller.find_contact_by_email(user_id, email)
            if contacts:
                print("Contato encontrado:")
                for contact in contacts:
                    print(contact)
            else:
                print("Nenhum contato encontrado com o e-mail especificado.")
        except Exception as e:
            print(f"Erro ao buscar contato por e-mail: {e}")

    def update_contact(self):
        print("\nAtualizar Contato")
        user_id = input("ID do usuário: ")
        contact_id = input("ID do contato: ")
        new_email = input("Novo e-mail do contato (deixe em branco para não alterar): ")
        new_phone_number = input("Novo número de telefone do contato (deixe em branco para não alterar): ")

        try:
            if new_email or new_phone_number:
                if self.contact_controller.update_contact(user_id, contact_id, new_email, new_phone_number):
                    print("Contato atualizado com sucesso!")
                else:
                    print("Erro ao atualizar o contato.")
            else:
                print("Nada para atualizar.")
        except Exception as e:
            print(f"Erro ao atualizar o contato: {e}")

    def delete_contact(self):
        print("\nExcluir Contato")
        contact_id = input("ID do contato: ")

        try:
            if self.contact_controller.delete_contact(contact_id):
                print("Contato excluído com sucesso!")
            else:
                print("Erro ao excluir o contato.")
        except Exception as e:
            print(f"Erro ao excluir o contato: {e}")