from flask import Flask


def init_app(app: Flask):
    from .estoque_view import bp_estoque
    app.register_blueprint(bp_estoque)
