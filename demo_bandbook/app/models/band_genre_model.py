from . import db


class BandGenreModel(db.Model):
    __tablename__ = 'band_genres'

    id = db.Column(db.Integer, primary_key=True)

    band_id = db.Column(db.Integer, db.ForeignKey(
        'bands.id', onupdate='CASCADE', ondelete='CASCADE'))
    genre_id = db.Column(db.Integer, db.ForeignKey(
        'genres.id', onupdate='CASCADE', ondelete='CASCADE'))
