from flask import Flask
from os import getenv

from config import config_selector
from blog.configurations import database
from blog.configurations import commands
from blog import views


def create_app():
    app = Flask(__name__)

    config_type = getenv('FLASK_ENV')
    app.config.from_object(config_selector[config_type])

    database.init_app(app)
    commands.init_app(app)
    views.init_app(app)

    return app
