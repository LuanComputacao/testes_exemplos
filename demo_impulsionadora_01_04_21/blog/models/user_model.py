from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)

    post_list = db.relationship(
        "PostModel",
        lazy="joined",
        backref=db.backref(
            "author",
            lazy="joined",
        ),
    )

    @property
    def password(self):
        raise AttributeError("Password is not an accessible attribute")

    @password.setter
    def password(self, new_password):
        self.password_hash = generate_password_hash(new_password)

    def check_password(self, password_to_check):
        return check_password_hash(self.password_hash, password_to_check)
