# Gerador de Senhas: Desenvolva um gerador de senhas que crie senhas aleatórias com um comprimento específico.
from password_generator import  PasswordGenerator


def main():
    print("Bem-vindo ao Gerador de Senhas!")

    while True:
        try:
            length = int(input("\nDigite o comprimento da senha desejada (ou digite 0 para sair): "))

            if length == 0:
                print("Obrigado por usar o Gerador de Senhas. Adeus!")
                break

            if length < 6:
                print("O comprimento mínimo da senha deve ser 6. Por favor, tente novamente.")
                continue

            password_generator = PasswordGenerator(length)
            password = password_generator.generate_password()

            print("Senha gerada:", password)

        except ValueError:
            print("Por favor, insira um valor válido para o comprimento da senha.")


if __name__ == "__main__":
    main()
