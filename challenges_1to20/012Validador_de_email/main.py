# Validador de E-mail: Construa um programa que valide se um endereço de e-mail inserido pelo usuário é válido.
from email_validator import EmailValidator


def main():
    email_validator = EmailValidator()

    print("Bem-vindo ao Validador de E-mail!")

    while True:
        email = input("Digite o endereço de e-mail que deseja validar (ou 'sair' para encerrar): ")

        if email.lower() == "sair":
            print("Obrigado por usar o Validador de E-mail!")
            break

        if email_validator.validate(email):
            print("O e-mail inserido é válido.")
        else:
            print("O e-mail inserido não é válido. Por favor, insira um endereço de e-mail válido.")


if __name__ == "__main__":
    main()

