import unittest
from model.codigo_fonte import CodigoFonte


class TestCodigoFonte(unittest.TestCase):
    def test_obter_classes_metodos(self):
        file_path = 'exemplo.py'
        with open(file_path, 'w') as file:
            file.write("class MinhaClasse:\n")
            file.write("    def meu_metodo(self):\n")
            file.write("        pass\n")

        codigo_fonte = CodigoFonte(file_path)
        classes_metodos = codigo_fonte.obter_classes_metodos()
        self.assertEqual(len(classes_metodos), 1)
        self.assertEqual(classes_metodos[0], ('MinhaClasse', 'meu_metodo'))

        import os
        os.remove(file_path)


if __name__ == '__main__':
    unittest.main()
