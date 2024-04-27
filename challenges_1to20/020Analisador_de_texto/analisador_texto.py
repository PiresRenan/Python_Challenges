class AnalisadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def contar_palavras(self):
        return len(self.texto.split())

    def contar_frases(self):
        return self.texto.count('.') + self.texto.count('!') + self.texto.count('?')

    def contar_paragrafos(self):
        return self.texto.count('\n\n') + 1
