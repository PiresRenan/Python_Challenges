from messages import *


class IMCCalculator:
    def calculate_imc(self, weight, height):
        # Calcula o IMC
        imc = weight / (height ** 2)
        return imc


def main():
    print("Bem-vindo à Calculadora de IMC!")
    calculator = IMCCalculator()

    # Solicita ao usuário o peso e a altura
    weight = float(input("Digite seu peso em kg: "))
    height = float(input("Digite sua altura em metros: "))

    # Calcula o IMC
    imc = calculator.calculate_imc(weight, height)

    # Exibe o resultado
    print(f"Seu IMC é: {imc:.2f}")

    # Exibe a classificação do IMC
    if imc < 18.5:
        print(UNDERWEIGHT_MESSAGE)
        for tip in UNDERWEIGHT_TIPS:
            print(tip)
        print(UNDERWEIGHT_RISK)
    elif imc < 25:
        print(NORMAL_WEIGHT_MESSAGE)
        for tip in NORMAL_WEIGHT_TIPS:
            print(tip)
    elif imc < 30:
        print(OVERWEIGHT_MESSAGE)
        for tip in OVERWEIGHT_TIPS:
            print(tip)
        print(OVERWEIGHT_RISK)
    else:
        print(OBESE_MESSAGE)
        for tip in OBESE_TIPS:
            print(tip)
        print(OBESE_RISK)


if __name__ == "__main__":
    main()
