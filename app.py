import flask
from flask import Flask
import translater

app = app = Flask(__name__)

@app.route('/')
def main():
    json_data = flask.request.json
    data = json_data["data"]
    return translater.weirdify(data)

if __name__ == '__main__':
    app.run()
