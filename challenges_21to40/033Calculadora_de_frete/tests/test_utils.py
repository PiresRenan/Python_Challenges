import unittest
from utils import Utils


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.addr1 = Utils()

    def test_get_address_info(self):
        expected_result = {
            "cep": "02535-040", "logradouro": "Rua Raul Jordão", "complemento": "",
            "bairro": "Parque Peruche", "localidade": "São Paulo", "uf": "SP", "ibge": "3550308",
            "gia": "1004", "ddd": "11", "siafi": "7107"
        }
        result = get_address_from_zipcode("02535040")
        self.assertEqual(result, expected_result)
