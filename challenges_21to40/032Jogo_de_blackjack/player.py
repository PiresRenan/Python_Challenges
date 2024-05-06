class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def get_hand_value(self):
        value = 0
        num_aces = 0
        for card in self.hand:
            if card.rank.isdigit():
                value += int(card.rank)
            elif card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                num_aces += 1
                value += 11
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def __str__(self):
        return f"Mão de {self.name}: {', '.join(str(card) for card in self.hand)}. Valor total: {self.get_hand_value()}"


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def show_partial_hand(self):
        return f"Mão do Dealer: {self.hand[0]} e [Carta Escondida]"

    def __str__(self):
        return f"{' '.join(str(card) for card in self.hand[1:])}. Valor total: {self.get_hand_value()}"
