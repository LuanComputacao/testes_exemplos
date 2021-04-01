from flask import Flask
from flask.cli import AppGroup
from sqlalchemy import and_
from click import argument
from faker import Faker
from random import randint
from typing import List

from blog.models.user_model import UserModel
from blog.models.post_model import PostModel
from blog.models.profile_model import ProfileModel


def cli_user(app: Flask):
    cli_group_user = AppGroup("user")

    @cli_group_user.command("create")
    @argument("quantity")
    def cli_user_bulk_create(quantity):
        session = app.db.session
        fake = Faker()
        users_to_insert = (
            UserModel(nickname=fake.name(), email=fake.unique.email())
            for _ in range(int(quantity))
        )
        for index, user in enumerate(users_to_insert):
            user.password = fake.text()[:15]
            session.add(user)
            if index % 50 == 0:
                session.commit()
        session.commit()

    app.cli.add_command(cli_group_user)


def cli_post(app: Flask):
    cli_group_post = AppGroup("post")

    @cli_group_post.command("create")
    @argument("quantity", nargs=1)
    @argument("user_scope", nargs=1)
    def cli_post_bulk_create(quantity, user_scope):
        fake = Faker()
        session = app.db.session

        n_range = [int(n) for n in user_scope.split("-")]

        users_in_chunck: List[UserModel] = (
            session.query(UserModel)
            .filter(and_(UserModel.id >= n_range[0], UserModel.id <= n_range[1]))
            .all()
        )

        user_post_list = lambda: (
            PostModel(title=fake.sentence(), content=fake.text())
            for _ in range(int(quantity))
        )

        for user in users_in_chunck:
            user.post_list = [*user.post_list, *list(user_post_list())]
            session.add(user)
            session.commit()
        session.commit()

    app.cli.add_command(cli_group_post)


def cli_profile(app: Flask):
    cli_group_profile = AppGroup("profile")

    @cli_group_profile.command("create")
    @argument("user_scope", nargs=1)
    def cli_profile_bulk_create(user_scope):
        fake = Faker()
        session = app.db.session

        n_range = [int(n) for n in user_scope.split("-")]

        users_in_chunck: List[UserModel] = (
            session.query(UserModel)
            .filter(and_(UserModel.id > n_range[0], UserModel.id < n_range[1]))
            .all()
        )

        user_profile = lambda: ProfileModel(age=randint(10, 95), bio=fake.text())

        for user in users_in_chunck:
            user.profile = user_profile()
            session.add(user)
            session.commit()
        session.commit()

    app.cli.add_command(cli_group_profile)


def init_app(app: Flask):
    cli_user(app)
    cli_post(app)
    cli_profile(app)
