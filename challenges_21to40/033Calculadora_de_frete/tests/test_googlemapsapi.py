import os
import time
import unittest
import googlemaps
from dotenv import load_dotenv

load_dotenv()


class DistanceMatrixTest(unittest.TestCase):
    def setUp(self):
        self.client = googlemaps.Client(os.getenv('GOOGLEAPI_KEY'))

    def test_basic_params(self):
        origins = [
            "Perth, Australia",
            "Sydney, Australia",
            "Melbourne, Australia",
            "Adelaide, Australia",
            "Brisbane, Australia",
            "Darwin, Australia",
            "Hobart, Australia",
            "Canberra, Australia",
        ]
        destinations = [
            "Uluru, Australia",
            "Kakadu, Australia",
            "Blue Mountains, Australia",
            "Bungle Bungles, Australia",
            "The Pinnacles, Australia",
        ]

        matrix = self.client.distance_matrix(origins, destinations)

        print(matrix)
        #
        # self.assertEqual(1, len(responses.calls))
        # self.assertURLEqual(
        #     "https://maps.googleapis.com/maps/api/distancematrix/json?"
        #     "key=%s&origins=Perth%%2C+Australia%%7CSydney%%2C+"
        #     "Australia%%7CMelbourne%%2C+Australia%%7CAdelaide%%2C+"
        #     "Australia%%7CBrisbane%%2C+Australia%%7CDarwin%%2C+"
        #     "Australia%%7CHobart%%2C+Australia%%7CCanberra%%2C+Australia&"
        #     "destinations=Uluru%%2C+Australia%%7CKakadu%%2C+Australia%%7C"
        #     "Blue+Mountains%%2C+Australia%%7CBungle+Bungles%%2C+Australia"
        #     "%%7CThe+Pinnacles%%2C+Australia" % self.key,
        #     responses.calls[0].request.url,
        # )