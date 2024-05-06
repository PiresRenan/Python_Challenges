import pytest
from models.crawler import WebCrawler


class TestWebCrawler:
    @pytest.fixture
    def web_crawler(self):
        return WebCrawler("https://pt.wikipedia.org/wiki/Memória_bolha")

    def test_extract_information_success(self, web_crawler):
        result = web_crawler.extract_information()
        assert result == "Informações extraídas com sucesso!"

    def test_extract_information_failure(self, web_crawler, monkeypatch):
        def mock_get(*args, **kwargs):
            raise Exception("Mocked HTTP Error")
        monkeypatch.setattr("requests.get", mock_get)
        result = web_crawler.extract_information()
        assert "Erro ao acessar a página da web" in result


