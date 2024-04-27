# Cronômetro: Escreva um cronômetro que conte o tempo decorrido em segundos, minutos e horas.
from cronos import Cronometro


def main():
    cronometro = Cronometro()

    while True:
        print("Opções:")
        print("1. Iniciar cronômetro")
        print("2. Parar cronômetro")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cronometro.iniciar_cronometro()
            print("Cronômetro iniciado.")
        elif opcao == "2":
            cronometro.parar_cronometro()
            print(cronometro.calcular_tempo_decorrido())
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
