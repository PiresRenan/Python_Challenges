import unittest
from model.documentacao import Documentacao


class TestDocumentacao(unittest.TestCase):
    def test_gerar_documentacao(self):
        classes_metodos = [('MinhaClasse', 'meu_metodo')]

        documentacao = Documentacao(classes_metodos)
        result = documentacao.gerar_documentacao()

        expected_result = "Classe: MinhaClasse\nMétodo: meu_metodo\n\n"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
