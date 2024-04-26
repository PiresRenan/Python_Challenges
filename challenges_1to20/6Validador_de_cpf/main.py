# Validador de CPF: Escreva um programa que valide se um CPF inserido pelo usuário é válido ou não.
from cpf_validator import CPFValidator


def main():
    print("Bem-vindo ao Validador de CPF!")

    while True:
        cpf = input("\nDigite o CPF a ser validado (ou digite 'sair' para encerrar): ")

        if cpf.lower() == "sair":
            print("Obrigado por usar o Validador de CPF. Adeus!")
            break

        validator = CPFValidator(cpf)
        if validator.is_valid():
            print("CPF válido.")
        else:
            print("CPF inválido.")


if __name__ == "__main__":
    main()
