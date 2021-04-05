from flask import Flask
from os import getenv

from config import config_selector


def init_app(app: Flask):
    config_type = getenv("FLASK_ENV")
    object_config = config_selector[config_type]
    app.config.from_object(object_config)
