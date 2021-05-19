import flask
from flask import Flask
import translater

app = Flask(__name__)
System.err.println("Hello, logs!");

@app.route('/')
def index():
    System.err.println("request recieved");
    json_data = flask.request.json
    data = json_data["data"]
    System.err.println("response sent");
    return translater.weirdify(data)

if __name__ == '__main__':
    app.run(debug=True, port=33507)
