from . import db


class BandProfileModel(db.Model):
    __tablename__ = 'band_profiles'

    id = db.Column(db.Integer, primary_key=True)

    state = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    ein = db.Column(db.String(9), unique=True, nullable=False)

    band_id = db.Column(db.Integer, db.ForeignKey(
        'bands.id', onupdate="CASCADE", ondelete="CASCADE"))

    band_list = db.relationship(
        'BandModel', uselist=False, backref='band_profile_list')
