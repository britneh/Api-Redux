from flask import Flask
from web_app.routes.home_routes import home_routes

from flask_sqlalchemy import SQLalchemy
from flask_migrate import Migrate

DATABASE_URI = "sqlite:///twitbrit.db" #creating database 

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] =False

    app.register_blueprint(home_routes)

    return app