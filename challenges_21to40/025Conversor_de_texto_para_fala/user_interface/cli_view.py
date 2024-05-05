class CommandLineInterface:
    def __init__(self):
        pass

    def get_user_input(self):
        return input("Digite o texto a ser convertido em fala: ")

    def display_output(self, speech):
        print("Fala gerada:\n")