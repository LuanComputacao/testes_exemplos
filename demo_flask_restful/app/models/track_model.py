from . import db


class TrackModel(db.Model):
    __tablename__ = "tracks"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120), nullable=False)
    album = db.Column(db.String(120), nullable=False)
