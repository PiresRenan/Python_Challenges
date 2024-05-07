import os
import unittest
import googlemaps
from dotenv import load_dotenv
import utils

load_dotenv()


class DistanceMatrixTest(unittest.TestCase):
    def setUp(self):
        self.addr1 = utils.get_address_from_zipcode("02535040")
        self.addr2 = utils.get_address_from_zipcode("08215450")
        self.client = googlemaps.Client(os.getenv('GOOGLEAPI_KEY'))

    def test_basic_params(self):
        local_orig = self.addr1['localidade']
        uf_orig = self.addr1['uf']

        local_dest = self.addr2['localidade']
        uf_dest = self.addr2['uf']

        origins = local_orig + '+' + uf_orig
        destinations = local_dest + '+' + uf_dest

        expected_results = {
            'destination_addresses': ['São Luís, State of Maranhão, Brazil'],
            'origin_addresses': ['São Paulo, State of São Paulo, Brazil'],
            'rows': [{'elements':
                          [{'distance':
                                {'text': '3,008 km', 'value': 3007526},
                            'duration':
                                {'text': '1 day 15 hours', 'value': 140554},
                            'status': 'OK'}
                           ]}],
            'status': 'OK'}

        matrix = self.client.distance_matrix(origins, destinations)
        print(matrix)
