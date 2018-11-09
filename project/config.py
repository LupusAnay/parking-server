import os

basedir = os.path.abspath(os.path.dirname(__file__))
POSTGRES = {
    'user': 'lupusanay',
    'pw': 'pass123',
    'db': 'parking',
    'host': 'localhost',
    'port': '5432',
}
host = '0.0.0.0'
port = 8080


class BaseConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
