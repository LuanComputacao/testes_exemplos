from flask import Blueprint, render_template, request
from handlers.http_handlers import json_de_sucesso
from http import HTTPStatus

bp_home = Blueprint('home', __name__)


@bp_home.route('/')
def home():
    return render_template('index.html')


@bp_home.route('/', methods=['POST'])
def home_post():
    if request.headers.get('Content-Type') == 'application/json':

        numeros = request.get_json()
        resultado = numeros.get('n1') + numeros.get('n2')
        return json_de_sucesso(resultado)

    return '', HTTPStatus.BAD_REQUEST
