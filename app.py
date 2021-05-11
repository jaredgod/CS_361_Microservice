import flask
from flask import Flask
import translater

app = app = Flask(__name__)

@app.route('/')
def main():
    return translater.weirdify('Hello World')

if __name__ == '__main__':
    app.run()
