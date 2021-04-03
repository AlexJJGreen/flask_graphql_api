from flask import Flask
from config import Config

# import instances
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_graphql import GraphQLView

# import blueprints
from app.database_logic import database_logic
from app.graphql_logic import graphql_logic

# import db instances
from app.database_logic.models import db

migrate = Migrate()


# init intances

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    # init databases and migrations
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # create database
        db.create_all()

        # register blueprints
        app.register_blueprint(graphql_logic, url_prefix="/graphql")
        app.register_blueprint(database_logic, url_prefix="/database_logic")

        from app import routes

        return app