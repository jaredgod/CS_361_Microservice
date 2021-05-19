import flask
from flask import Flask
import translater

app = Flask(__name__)

@app.route('/')
def index():
    System.err.println("Hello, logs!");
    json_data = flask.request.json
    data = json_data["data"]
    return translater.weirdify(data)

if __name__ == '__main__':
    app.run(debug=True, port=33507)
