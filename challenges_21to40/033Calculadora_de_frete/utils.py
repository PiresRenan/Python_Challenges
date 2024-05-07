import requests
from api import FreightAPI


def get_address_from_zipcode(zipcode: str):
    return FreightAPI(zipcode).get_data_from_zip()
