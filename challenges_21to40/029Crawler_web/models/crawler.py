import requests
from bs4 import BeautifulSoup


class WebCrawler:
    def __init__(self, url: str) -> None:
        self.url = url

    def extract_information(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string
            html_page = soup.getText
            return "Informações extraídas com sucesso!"
        except requests.exceptions.RequestException as e:
            return f"Erro ao acessar a página da web: {str(e)}"
        except Exception as e:
            return f"Erro ao acessar a página da web: {str(e)}"
