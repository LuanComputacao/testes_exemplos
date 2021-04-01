from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from blog.models.user_model import UserModel
    from blog.models.post_model import PostModel
    from blog.models.profile_model import ProfileModel
