from flask import Flask

from blog import configurations
from blog.configurations import database
from blog.configurations import commands


def create_app():
    app = Flask(__name__.split(".")[0].title())

    configurations.init_app(app)
    database.init_app(app)
    commands.init_app(app)

    return app
