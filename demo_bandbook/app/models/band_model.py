from . import db

class BandModel(db.Model):
    __tablename__ = "bands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
