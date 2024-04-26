# Contador de Palavras: Escreva um programa que conte o número de palavras em um texto inserido pelo usuário.
from word_counter import WordCounter


def main():
    print("Bem-vindo ao Contador de Palavras!")

    while True:
        text = input("\nPor favor, insira o texto (ou digite 'sair' para encerrar): ")

        if text.lower() == "sair":
            print("Obrigado por usar o Contador de Palavras. Adeus!")
            break

        contador_de_palavras = WordCounter(text)
        palavras_contadas = contador_de_palavras.count_words()

        print("Número de palavras no texto:", palavras_contadas)


if __name__ == "__main__":
    main()
