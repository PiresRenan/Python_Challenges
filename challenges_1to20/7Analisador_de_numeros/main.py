# Analisador de Números: Desenvolva um programa que analise uma lista de números e exiba a média, a mediana e o
# desvio padrão.
import statistics
from number_analyzer import NumberAnalyzer


def main():
    print("Bem-vindo ao Analisador de Números!")

    while True:
        try:
            input_str = input("\nDigite uma lista de números separados por espaço (ou digite 'sair' para encerrar): ")

            if input_str.lower() == "sair":
                print("Obrigado por usar o Analisador de Números. Adeus!")
                break

            numbers = [float(num) for num in input_str.split()]
            analyzer = NumberAnalyzer(numbers)

            mean = analyzer.calculate_mean()
            median = analyzer.calculate_median()
            std_deviation = analyzer.calculate_standard_deviation()

            print("\nResultados:")
            print("Média:", "{:.2}".format(mean))
            print("Mediana:", "{:.2f}".format(median))
            print("Desvio Padrão:", "{:.2f}".format(std_deviation))

        except statistics.StatisticsError as e:
            print("Erro ao calcular estatísticas:", e)
        except ValueError:
            print("Por favor, insira uma lista válida de números separados por espaço.")


if __name__ == "__main__":
    main()
