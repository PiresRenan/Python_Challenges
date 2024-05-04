import unittest
from data.data_manager import DataManager


class TestDataManager(unittest.TestCase):
    def test_load_data_from_file(self):
        # Testa se os dados são carregados corretamente de um arquivo
        file_path = 'data/test_data.csv'
        data_manager = DataManager()
        data = data_manager.load_data(file_path)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_process_data(self):
        # Testa se os dados são processados corretamente
        raw_data = [('A', 10), ('B', 20), ('C', 30)]
        expected_processed_data = {'labels': ['A', 'B', 'C'], 'values': [10, 20, 30]}
        data_manager = DataManager()
        processed_data = data_manager.process_data(raw_data)
        self.assertIsNotNone(processed_data)
        self.assertIsInstance(processed_data, dict)
        self.assertDictEqual(processed_data, expected_processed_data)


if __name__ == '__main__':
    unittest.main()
