from urllib.parse import urlparse


class URLAnalyzer:
    def analyze_url(self, url):
        # Analisa a URL
        parsed_url = urlparse(url)

        # Extrai as diferentes partes da URL
        scheme = parsed_url.scheme
        netloc = parsed_url.netloc
        path = parsed_url.path
        params = parsed_url.params
        query = parsed_url.query
        fragment = parsed_url.fragment

        return scheme, netloc, path, params, query, fragment
