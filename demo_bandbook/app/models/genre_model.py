from . import db


class GenreModel(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    band_list = db.relationship(
        'BandModel', backref='genre_list', secondary='band_genres'
    )
