import unittest

import pandas as pd

from data.data_manager import DataManager


class TestDataManager(unittest.TestCase):
    def test_load_data_from_file(self):
        file_path = '../data/kid_iq.csv'
        data_manager = DataManager(file_path)
        data = data_manager.load_data()
        print(data.info())
        self.assertIsNotNone(data)
        self.assertTrue(isinstance(data, pd.DataFrame))
        self.assertGreater(len(data), 0)

    def test_process_data(self):
        child_iq_expected = [65, 98, 85, 83, 115]
        mother_education_expected = [1, 1, 1, 1, 1]
        mother_iq_expected = [121.1175286, 89.36188171, 115.4431649, 99.44963944, 92.74571]
        mother_job_expected = [4, 4, 4, 3, 4]
        mother_ages_expected = [27, 25, 27, 25, 27]
        file_path = '../data/kid_iq.csv'
        data_manager = DataManager(file_path)
        data = data_manager.process_data(data_manager.load_data())
        for n in range(0, 5):
            self.assertEqual(data['child_IQ_score'][n], child_iq_expected[n])
        for n in range(0, 5):
            self.assertEqual(data['mother_education'][n], mother_education_expected[n])
        for n in range(0, 5):
            self.assertEqual(data['mother_iq'][n], mother_iq_expected[n])
        for n in range(0, 5):
            self.assertEqual(data['mother_job'][n], mother_job_expected[n])
        for n in range(0, 5):
            self.assertEqual(data['mother_age'][n], mother_ages_expected[n])


if __name__ == '__main__':
    unittest.main()
