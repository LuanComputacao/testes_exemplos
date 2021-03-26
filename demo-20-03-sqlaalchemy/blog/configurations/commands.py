from flask import Flask
from flask.cli import AppGroup


def init_app(app: Flask):
    cli_db_group = AppGroup('db')

    @cli_db_group.command('create')
    def cli_db_create_all():
        app.db.create_all()
    
    @cli_db_group.command('drop')
    def cli_db_drop_all():
        app.db.drop_all()

    app.cli.add_command(cli_db_group)
