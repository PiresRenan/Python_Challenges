from deck import Deck
from player import Player, Dealer


class Game:
    def __init__(self, player: str):
        self.deck = Deck()
        self.player = Player(player)
        self.dealer = Dealer()
        self.deck.shuffle()

    def deal_initial_cards(self):
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

    def player_turn(self):
        while self.player.get_hand_value() < 21:
            print(self.player)
            choice = input("Mais uma carta ou manter? (c/m): ").strip().lower()
            if choice == 'c':
                self.player.add_card(self.deck.deal())
            elif choice == 'm':
                break
            else:
                print("Escolha inválida. Digite 'c' para mais uma carta ou 'm' para manter.")

    def dealer_turn(self):
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card(self.deck.deal())

    def determine_winner(self):
        player_score = self.player.get_hand_value()
        dealer_score = self.dealer.get_hand_value()

        if player_score > 21:
            return "Dealer venceu! Jogador superado."
        elif dealer_score > 21:
            return "Jogador venceu! Dealer superado."
        elif player_score == dealer_score:
            return "Empate!"
        elif player_score > dealer_score:
            return "Jogador venceu!"
        else:
            return "Dealer venceu!"

    def play(self):
        print("Bem vindo ao Blackjack!")
        self.deal_initial_cards()
        print(self.dealer.show_partial_hand())

        self.player_turn()

        if self.player.get_hand_value() <= 21:
            self.dealer_turn()
            print("Mão do Dealer:")
            print(self.dealer)

        print(self.determine_winner())


if __name__ == "__main__":
    player_name = input("Digite seu nome: ")
    game = Game(player_name)
    game.play()
