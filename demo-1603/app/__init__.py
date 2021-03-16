from flask import Flask
from .views import init_app


def create_app():
    app = Flask(__name__)

    app.config['JSON_SORT_KEYS'] = False

    init_app(app)

    return app
