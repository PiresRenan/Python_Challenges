from model.models import CreditCard, Validator


class CreditCardController:
    @staticmethod
    def validate(number: str) -> bool:
        card = CreditCard(number)
        return Validator.validate_credit_card(card)
