import flask
from flask import Flask
import translater

app = app = Flask(__name__)

@app.route('/')
def main():
    json_data = flask.request.json
    data = json_data["data"]
    return translater.weirdify(data)

app.run(host='127.0.0.1', port=8081)