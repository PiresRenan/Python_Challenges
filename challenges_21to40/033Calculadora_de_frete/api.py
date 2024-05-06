import requests


class FreightAPI:
    def __init__(self, zip_code: str):
        self.api_url = f"https://viacep.com.br/ws/{zip_code}/json/"

    def get_shipping_cost(self, origin_address, destination_address, weight):
        # Implemente a lógica para consultar a API de frete e obter o custo de envio
        pass
