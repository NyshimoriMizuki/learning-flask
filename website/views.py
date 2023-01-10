from flask import redirect, url_for, render_template
from flask import Blueprint

views = Blueprint("views", __name__)


@views.route("/")
def blank():
    return redirect(url_for("views.home"))


@views.route("/home")
def home():
    return render_template("home.html", title="Home")
