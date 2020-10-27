import logging

from flask import Flask
from flask_cors import CORS
from flask.logging import default_handler

from . import settings
from .meta import SingletonMeta
from .database import db
from .serializers import ma
from .migrate import migrate

from routes import url_prefix_x_blueprint


class Application(metaclass=SingletonMeta):
    """."""

    def __init__(self, name) -> None:
        """."""

        self.app: Flask = Flask(name)
        self.app.config.update(
            BASE_DIR=settings.BASE_DIR,
            HOST="0.0.0.0",
            PORT=settings.PORT,
            DEBUG=settings.DEBUG,
            ENV=settings.ENV,
            SQLALCHEMY_DATABASE_URI=settings.SQLALCHEMY_DATABASE_URI,
            SQLALCHEMY_TRACK_MODIFICATIONS=settings.SQLALCHEMY_TRACK_MODIFICATIONS
        )

        if settings.ENV == 'production':
            self.app.logger.removeHandler(default_handler)
            self.app.logger.setLevel(logging.DEBUG)
            self.app.logger.addHandler(settings.LOGGING_HANDLER)

        CORS(self.app)
        db.init_app(self.app)
        ma.init_app(self.app)
        migrate.init_app(self.app, db)

        with self.app.app_context():
            db.create_all()

        for url_prefix, blueprint in url_prefix_x_blueprint.items():
            self.app.register_blueprint(blueprint, url_prefix=url_prefix)

    def __call__(self, *args, **kwargs) -> Flask:
        """."""

        return self.app
