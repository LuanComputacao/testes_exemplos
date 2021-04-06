from . import db


class MusicModel(db.Model):
    __tablename__ = 'musics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    band_id = db.Column(db.Integer, db.ForeignKey(
        'bands.id', onupdate='CASCADE', ondelete='CASCADE'))
