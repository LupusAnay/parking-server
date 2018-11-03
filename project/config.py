import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_url = 'oracle+cx_oracle://system:oracle@localhost:49161/'
database_name = 'parking_database'


class BaseConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = database_url + database_name


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = database_url + database_name
