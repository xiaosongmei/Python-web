#coding=utf-8
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='119.23.232.25', port=9409)