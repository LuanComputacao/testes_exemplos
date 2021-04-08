from flask import Flask
from os import getenv

from app.configurations import database
from app.configurations import migrations
from app.configurations import serializer
from app.configurations import views


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    database.init_app(app)
    migrations.init_app(app)
    serializer.init_app(app)
    views.init_app(app)

    return app
