from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

from .views import views
from .auth import auth


def create_site():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "test"

    app.register_blueprint(views, url_prefix="/")

    return app
