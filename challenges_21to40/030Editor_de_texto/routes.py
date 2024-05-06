from flask import Flask, render_template, request, redirect, url_for
from model.textfile import TextFile

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/save', methods=['POST'])
def save():
    filename = request.form['filename']
    content = request.form['content']
    file = TextFile(filename, content)
    file.save(filename)
    return redirect(url_for('editor'))


@app.route('/load', methods=['POST'])
def load():
    filename = request.form['filename']
    file = TextFile.load(filename)
    return render_template('editor.html', filename=filename, content=file.content)


if __name__ == '__main__':
    app.run(debug=True)
