from flask import redirect, url_for, render_template
from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route("/login")
def login():
    return render_template("login.html")
