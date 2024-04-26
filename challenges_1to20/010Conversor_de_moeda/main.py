# Conversor de Moeda: Desenvolva um conversor de moeda que converta entre diferentes unidades monetárias
from currency_converter import CurrencyConverter


def main():
    currency_converter = CurrencyConverter()

    print("Bem-vindo ao Conversor de Moeda!")

    while True:
        amount = float(input("Digite o valor a ser convertido: "))
        from_currency = input("Digite a moeda de origem (ex: USD, EUR, BRL): ").upper()
        to_currency = input("Digite a moeda de destino (ex: USD, EUR, BRL): ").upper()

        converted_amount = currency_converter.convert(amount, from_currency, to_currency)

        if converted_amount is not None:
            print(f"{amount:.2f} {from_currency} equivalem a {converted_amount:.2f} {to_currency}")
        else:
            print("Não foi possível realizar a conversão. Verifique as moedas informadas.")

        choice = input("Deseja fazer outra conversão? (s/n): ")
        if choice.lower() != "s":
            print("Obrigado por usar o Conversor de Moeda!")
            break


if __name__ == "__main__":
    main()
