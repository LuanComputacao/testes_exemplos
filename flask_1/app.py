from flask import Flask, request, render_template
from environs import Env
from http import HTTPStatus

from services.devs_services import DevsServices
from handlers.http_handlers import json_de_sucesso

from views.home_view import bp_home
from views.devs_view import bp_devs


def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_devs)

    return app
