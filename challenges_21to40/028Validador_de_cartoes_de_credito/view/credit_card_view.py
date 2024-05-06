class CreditCardView:
    @staticmethod
    def get_user_input() -> str:
        return input("Digite o número do cartão(ou 'sair' para sair): ")

    @staticmethod
    def display_validation_result(is_valid: bool) -> None:
        if is_valid:
            print("O número do cartão de crédito é válido.")
        else:
            print("O número do cartão de crédito é inválido.")
