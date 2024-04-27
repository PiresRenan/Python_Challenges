# Analisador de Texto: Construa um programa que analise um texto e retorne o número de palavras, frases e parágrafos.
from analisador_texto import AnalisadorTexto
import sys



def main():
    texto = input("Digite o texto a ser analisado:\n")

    analisador = AnalisadorTexto(texto)

    palavras = analisador.contar_palavras()
    frases = analisador.contar_frases()
    paragrafos = analisador.contar_paragrafos()

    print(f"Número de palavras: {palavras}")
    print(f"Número de frases: {frases}")
    print(f"Número de parágrafos: {paragrafos}")


if __name__ == "__main__":
    main()
