import unittest
from unittest.mock import patch
from io import StringIO
from view.documentacao_view import DocumentacaoView


class TestDocumentacaoView(unittest.TestCase):
    def test_exibir_documentacao(self):
        documentacao = 'Documentação gerada'
        expected_output = 'Documentação gerada\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            DocumentacaoView().exibir_documentacao(documentacao)

            output = fake_out.getvalue()

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()