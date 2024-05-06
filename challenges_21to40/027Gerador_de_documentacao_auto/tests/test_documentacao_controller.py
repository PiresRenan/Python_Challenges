import unittest
from controller.documentacao_controller import DocumentacaoController


class TestDocumentacaoController(unittest.TestCase):
    def test_gerar_documentacao(self):
        file_path = 'exemplo.py'
        with open(file_path, 'w') as file:
            file.write("class MinhaClasse:\n")
            file.write("    def meu_metodo(self):\n")
            file.write("        pass\n")

        documetacao_controller = DocumentacaoController(file_path)
        result = documetacao_controller.gerar_documentacao()
        expected_result = "Classe: MinhaClasse\nMétodo: meu_metodo\n\n"

        self.assertEqual(result, expected_result)

        import os
        os.remove(file_path)


if __name__ == '__main__':
    unittest.main()
