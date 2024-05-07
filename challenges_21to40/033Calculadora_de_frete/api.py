import requests


class FreightAPI:
    def __init__(self, zip_code: str):
        self.api_url = f"https://viacep.com.br/ws/{zip_code}/json/"

    def get_data_from_zip(self):
        data = requests.get(self.api_url).json()
        return data
