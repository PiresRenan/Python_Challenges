# Conversor de Unidades: Desenvolva um programa que converta entre diferentes unidades de medida (por exemplo,
# metros para quilômetros, litros para galões, etc.).
from converter_factory import ConverterFactory


def print_menu():
    print("Opções de conversão:")
    print("1. Metros para Quilômetros")
    print("2. Metros para Centímetros")
    print("3. Metros para Milímetros")
    print("4. Metros para Milhas")
    print("5. Metros para Jardas")
    print("6. Metros para Polegadas")
    print("7. Galões para Litros")
    print("8. Quilos para Gramas")
    print("9. Quilos para Toneladas")
    print("10. Litros para Galões")
    print("S. Sair")


def main():
    print("Bem-vindo ao Conversor de Unidades!")
    converter_factory = ConverterFactory()

    while True:
        print_menu()
        choice = input("Escolha uma opção: ")

        if choice.upper() == "S":
            print("Saindo do programa...")
            break

        try:
            value = float(input("Digite a quantidade: "))
            converter = converter_factory.create_converter(choice)
            if converter:
                result = converter.convert(value)
                print(f"Resultado: {result}\n")
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
