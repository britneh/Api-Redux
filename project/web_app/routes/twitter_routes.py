from flask import Blueprint

twitter_routes = Blueprint("twitter_routes", __name__)


@twitter_routes.route("/users")
def fetch_user():
    return "You've accessed fetch user, hooray!"