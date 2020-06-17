from web_app.models import db, migrate
from flask import Flask
from web_app.routes.home_routes import home_routes
from web_app.routes.twitter_routes import twitter_routes

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DATABASE_URI = "sqlite:///twitbrit.db" #creating database 

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] =False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(twitter_routes)

    return app
