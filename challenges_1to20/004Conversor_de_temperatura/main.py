# Conversor de Temperatura: Crie um conversor de temperatura que converta entre Celsius, Fahrenheit e Kelvin.
from temperature_converter import TemperatureConverter


def main():
    print("Bem-vindo ao Conversor de Temperatura!")

    while True:
        try:
            temperature = input("\nDigite a temperatura (ou digite 'sair' para encerrar): ")

            if temperature.lower() == "sair":
                print("Obrigado por usar o Conversor de Temperatura. Adeus!")
                break

            temperature = float(input("\nDigite a temperatura: "))
            scale = input("Digite a escala da temperatura (C - Celsius, F - Fahrenheit, K - Kelvin): ").strip().upper()

            converter = TemperatureConverter(temperature, scale)

            print("\nResultados:")
            print("Celsius:", converter.to_celsius())
            print("Fahrenheit:", converter.to_fahrenheit())
            print("Kelvin:", converter.to_kelvin())

        except ValueError:
            print("Por favor, insira um valor numérico para a temperatura.")
        except KeyError:
            print("Escala não suportada. Por favor, use 'C', 'F' ou 'K'.")


if __name__ == "__main__":
    main()
