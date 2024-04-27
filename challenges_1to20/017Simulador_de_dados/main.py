# Simulador de Dados: Crie um simulador de lançamento de dados que simule o lançamento de um ou mais dados.
from dice_simulator import DiceSimulator


def main():
    print("Bem-vindo ao Simulador de Dados!")
    simulator = DiceSimulator()

    # Solicita ao usuário o número de dados e faces
    num_dice = int(input("Digite o número de dados a serem lançados: "))
    num_faces = int(input("Digite o número de faces dos dados: "))

    # Simula o lançamento de dados
    rolls = simulator.roll_dice(num_dice, num_faces)

    # Exibe os resultados dos lançamentos
    print("Resultados dos lançamentos:")
    for i, roll in enumerate(rolls, 1):
        print(f"Dado {i}: {roll}")


if __name__ == "__main__":
    main()
