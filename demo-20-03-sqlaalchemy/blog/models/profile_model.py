from . import db


class ProfileModel(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    bio = db.Column(db.Text)
