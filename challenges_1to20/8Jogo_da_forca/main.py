# Jogo da Forca: Implemente o clássico jogo da forca onde o jogador deve adivinhar uma palavra oculta.
from hangmangame import HangmanGame


def main():
    game = HangmanGame()

    print("Bem-vindo ao Jogo da Forca!")

    while True:
        game.new_game()
        print("\nNova partida iniciada.")

        while not game.is_game_over():
            game.display_game_status()
            print("\nEscolha uma opção:")
            print("1. Tentar uma letra")
            print("2. Usar uma dica")
            print("3. Sair")

            choice = input("Digite o número da opção desejada: ")

            if choice == "1":
                guess = input("Digite uma letra: ").lower()
                game.guess(guess)
            elif choice == "2":
                game.give_hint()
            elif choice == "3":
                print("Obrigado por jogar!")
                return
            else:
                print("Opção inválida. Por favor, escolha uma das opções disponíveis.")

        play_again = input("Deseja jogar novamente? (s/n): ").lower()
        if play_again != "s":
            print("Obrigado por jogar!")
            break


if __name__ == "__main__":
    main()
