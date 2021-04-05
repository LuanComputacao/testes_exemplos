from os import getenv


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv("DB_URI_DEV")


class ProductionConfig(Config):
    ...


class TestConfig(Config):
    ...


config_selector = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestConfig,
}
