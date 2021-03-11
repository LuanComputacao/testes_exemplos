from flask import Flask
from http import HTTPStatus

app = Flask(__name__)


@app.route('/')
def home():
    return {'msg': 'nice!'},  HTTPStatus.OK
