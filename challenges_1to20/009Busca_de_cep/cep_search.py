import requests


class CEPSearch:
    def __init__(self):
        self.base_url = "https://viacep.com.br/ws/"

    def search(self, cep):
        url = f"{self.base_url}{cep}/json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return {
                "cep": data.get("cep"),
                "logradouro": data.get("logradouro"),
                "complemento": data.get("complemento"),
                "bairro": data.get("bairro"),
                "localidade": data.get("localidade"),
                "uf": data.get("uf"),
            }
        else:
            print("Erro ao buscar informações do CEP.")
            return None
