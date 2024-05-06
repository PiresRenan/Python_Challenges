from flask import Flask, request, jsonify
from controllers.crawler_controller import CrawlerController

app = Flask(__name__)
controller = CrawlerController()


@app.route('/')
def index():
    return 'Bem vindo ao Web Crawler App!'


@app.route('/crawl', methods=['POST'])
def crawl_website():
    if 'url' not in request.json:
        return jsonify({'error': 'URL não fornecida'}), 400

    url = request.json['url']
    result = controller.crawl_website(url)

    return jsonify({'result': result}), 200


if __name__ == '__main__':
    app.run(debug=True)
