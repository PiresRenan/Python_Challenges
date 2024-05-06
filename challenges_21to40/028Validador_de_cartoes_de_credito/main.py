from controller.credit_card_controller import CreditCardController
from view.credit_card_view import CreditCardView


def main():
    while True:
        card_number = CreditCardView.get_user_input()

        if card_number.lower() == 'sair':
            print("Encerrando o programa...")
            break

        is_valid = CreditCardController.validate(card_number)

        CreditCardView.display_validation_result(is_valid)


if __name__ == '__main__':
    main()
