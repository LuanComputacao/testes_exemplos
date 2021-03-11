from flask import Blueprint
from http import HTTPStatus
from handlers.http_handlers import json_de_sucesso
from services.devs_services import DevsServices


bp_devs = Blueprint('bp_devs', __name__)


@bp_devs.route('/devs/')
def devs_get():
    return json_de_sucesso(DevsServices.read_csv())


@bp_devs.route('/devs/<nome>')
def dev_by_name(nome=''):
    dev = DevsServices.verifica_se_existe_pelo_nome(nome)
    if len(dev) > 0:
        return json_de_sucesso(dev)

    response = {
        'status': 'Not found :P'
    }

    return response, HTTPStatus.NOT_FOUND
