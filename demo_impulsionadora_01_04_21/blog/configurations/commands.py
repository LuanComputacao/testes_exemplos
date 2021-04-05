from flask import Flask
from flask.cli import AppGroup
from click import argument
from faker import Faker

from blog.models.user_model import UserModel


def group_user(app: Flask):
    fake = Faker()
    session = app.db.session
    cli_group_user = AppGroup("user")

    @cli_group_user.command("create")
    @argument("quantity", nargs=1)
    @argument("pera", nargs=1)
    @argument("maca", nargs=1)
    def cli_user_create(quantity, pera, maca):
        print(quantity, pera, maca)
        for index in range(int(quantity)):
            new_user = UserModel(
                nickname=fake.name(),
                email=fake.unique.email(),
            )
            new_user.password = fake.text()[:15]

            session.add(new_user)
            if index % 10 == 0:
                session.commit()
        session.commit()

    app.cli.add_command(cli_group_user)


def group_db(app: Flask):
    cli_group_db = AppGroup("database")
    db = app.db

    @cli_group_db.command("create")
    def cli_db_create():
        db.create_all()

    @cli_group_db.command("drop")
    def cli_db_create():
        db.drop_all()

    app.cli.add_command(cli_group_db)


def init_app(app: Flask):
    group_db(app)
    group_user(app)
