#Calculadora Simples: Crie uma calculadora simples capaz de realizar operações básicas como adição, subtração, multiplicação e divisão.
from calculator import Calculator


def main():
    print("Bem-vindo à calculadora!")
    while True:
        try:
            print("\nEscolha a operação:")
            print("1. Adição")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("5. Sair")

            choice = int(input("Digite o número da operação desejada: "))

            if choice == 5:
                print("Obrigado por usar a calculadora. Adeus!")
                break

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            calc = Calculator()

            if choice == 1:
                print("Resultado:", calc.add(num1, num2))
            elif choice == 2:
                print("Resultado:", calc.subtract(num1, num2))
            elif choice == 3:
                print("Resultado:", calc.multiply(num1, num2))
            elif choice == 4:
                print("Resultado:", calc.divide(num1, num2))
            else:
                print("Opção inválida. Por favor, escolha uma das opções válidas.")

        except ValueError:
            print("Por favor, insira números válidos.")


if __name__ == "__main__":
    main()
