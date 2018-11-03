import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from project.views import parking_blueprint

app = Flask(__name__)
CORS(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

db = SQLAlchemy(app)

app.register_blueprint(parking_blueprint)
