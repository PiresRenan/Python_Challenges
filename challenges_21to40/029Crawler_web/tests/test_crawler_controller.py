from controllers.crawler_controller import CrawlerController


class TestCrawlerController:
    def test_crawl_website_success(self, monkeypatch):
        controller = CrawlerController()

        def mock_extract_information(url):
            return "Informações extraídas com sucesso!"

        monkeypatch.setattr("models.crawler.WebCrawler.extract_information", mock_extract_information)

        result = controller.crawl_website("https://pt.wikipedia.org/wiki/Memória_bolha")
        assert result == "Informações extraídas com sucesso!"

    def test_crawl_website_failure(self, monkeypatch):
        controller = CrawlerController()

        def mock_extract_information(url):
            return "Erro ao acessar a página da web: Mocked HTTP Error"

        monkeypatch.setattr("models.crawler.WebCrawler.extract_information", mock_extract_information)

        result = controller.crawl_website("invalid_url")
        assert result == "Erro ao acessar a página da web: Mocked HTTP Error"
