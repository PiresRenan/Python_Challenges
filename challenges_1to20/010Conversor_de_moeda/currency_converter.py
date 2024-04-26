from forex_python.converter import CurrencyRates


class CurrencyConverter:
    def __init__(self):
        self.currency_rates = CurrencyRates()

    def convert(self, amount, from_currency, to_currency):
        try:
            converted_amount = self.currency_rates.convert(from_currency, to_currency, amount)
            return converted_amount
        except ValueError as e:
            print("Erro:", e)
            return None
