from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from flask import redirect, url_for, render_template
from flask import request
from flask import Blueprint

from . import db
from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    messages = []

    if request.method == "POST":
        new_user = request.form.get("username")
        email = request.form.get("email")
        password = [request.form.get("make_pw"),
                    request.form.get("confirm_pw")]

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=new_user).first()
        if username_exists:
            messages.append("Username already in use")
        if email_exists:
            messages.append("Email already in use")
        if len(password) < 6:
            messages.append("Password is is too short")
        if password[0] != password[1]:
            messages.append("Passwords don't match")

        else:
            new_user = User(email=email,
                            username=new_user,
                            password=generate_password_hash(password[0], method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for("views.home"))

    return render_template("signup.html", title="Sign up", messages=messages)


@auth.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for("views.home"))
        message = "Email or password is wrong."

    return render_template("login.html", title="Login", message=message)


@login_required
@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("view.home"))
