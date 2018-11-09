import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.config.DevelopmentConfig'
)

app.config.from_object(app_settings)

db = SQLAlchemy(app)

# Need to create blueprint after db creation
from project.views import parking_blueprint

app.register_blueprint(parking_blueprint)
