class CreditCard:
    def __init__(self, number: str) -> None:
        self.number = number


class Validator:
    @staticmethod
    def validate_credit_card(card: CreditCard) -> bool:
        card_number = card.number.replace(" ", "").replace("-", "").replace(":", "").replace("(", "").replace(")", "")
        if not card_number.isdigit():
            return False
        if len(card_number) != 16:
            return False
        total = 0
        for i in range(0, 16, 2):
            soma = int(card_number[i]) * 2
            for digit in str(soma):
                total += int(digit)
        for i in range(1, 17, 2):
            soma = int(card_number[i])
            for digit in str(soma):
                total += int(digit)
        return total % 10 == 0

