# Gerador de Cartões de Visita: Crie um programa que gere cartões de visita com informações fornecidas pelo usuário.
from card_generator import CardGenerator


def main():
    print("Bem-vindo ao Gerador de Cartões de Visita!")

    generator = CardGenerator()

    name = input("Digite seu nome: ")
    title = input("Digite seu cargo: ")
    email = input("Digite seu e-mail: ")
    phone = input("Digite seu telefone: ")

    card = generator.generate_card(name, title, email, phone)
    print("Aqui está o seu cartão de visita:")
    print(card)

    print("Obrigado por usar o Gerador de Cartões de Visita!")


if __name__ == "__main__":
    main()
