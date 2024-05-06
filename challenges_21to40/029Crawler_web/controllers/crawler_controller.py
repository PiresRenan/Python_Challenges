from models.crawler import WebCrawler


class CrawlerController:
    def __init__(self):
        pass

    def crawl_website(self, url):
        crawler = WebCrawler(url)
        result = crawler.extract_information()
        return result
