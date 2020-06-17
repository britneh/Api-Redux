from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    return "You've accessed the index, hooray!"