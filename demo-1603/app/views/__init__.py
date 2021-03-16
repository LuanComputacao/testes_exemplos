from .home_view import bp as bp_home
from .character_view import bp as bp_char


def init_app(app):
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_char)
