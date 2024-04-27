# Adivinhe o Número: Escreva um jogo em que o computador escolhe um número aleatório e o jogador tenta adivinhar.
from guess_the_number import GuessTheNumber


def main():
    print("Bem-vindo ao Adivinhe o Número!")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar.")

    game = GuessTheNumber()

    while True:
        guess = int(input("Digite o seu palpite: "))

        result = game.guess(guess)
        print(result)

        if result == "Parabéns! Você acertou o número.":
            print(f"Você acertou em {game.get_attempts()} tentativas.")
            break


if __name__ == "__main__":
    main()
