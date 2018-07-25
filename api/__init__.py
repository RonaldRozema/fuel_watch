import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from api.models import db
from api.config import Config
from api.bike import bike_api

def create_app(test_config=None):

    # Creage and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # initialize db for app
    db.init_app(app)
    from api.models import bike
    migrate = Migrate(app, db)

    # register blueprints
    app.register_blueprint(bike_api)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello World!'
    
    return app