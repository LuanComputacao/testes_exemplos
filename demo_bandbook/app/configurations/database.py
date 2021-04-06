from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db
    from app.models.band_model import BandModel
    from app.models.band_profile_model import BandProfileModel
    from app.models.music_model import MusicModel
    from app.models.genre_model import GenreModel
    from app.models.band_genre_model import BandGenreModel