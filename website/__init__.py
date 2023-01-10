from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_site():
    from .auth import auth
    from .views import views
    from .models import User

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "xGiwNn7fag"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    create_database(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


def create_database(app):
    if not path.exists(f"website/data/{DB_NAME}"):
        with app.app_context():
            db.create_all()
        print("created database")
