import os
import logging
import configparser
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_cors import CORS
from flask.logging import default_handler

from utils.database import db, ma
from utils.migrate import migrate
from routes import url_prefix_x_blueprint


class Application(object):
    """."""

    INSTANCE = None
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ENV: str = os.environ.get('ENV', 'development')

    def __init__(self, name: str):
        """."""

        config: configparser.ConfigParser = self._get_config()
        handler: TimedRotatingFileHandler = self._get_logging_handler()

        self.app: Flask = Flask(name)
        self.app.config.update(
            BASE_DIR=self.BASE_DIR,
            HOST='0.0.0.0',
            PORT=config.getint('DEFAULT', 'PORT'),
            DEBUG=config.getboolean('DEFAULT', 'DEBUG'),
            ENV=config.get('DEFAULT', 'ENV'),
            SQLALCHEMY_DATABASE_URI=config.get('DEFAULT', 'SQLALCHEMY_DATABASE_URI'),
            SQLALCHEMY_TRACK_MODIFICATIONS=config.getboolean('DEFAULT', 'SQLALCHEMY_TRACK_MODIFICATIONS')
        )

        if self.ENV == 'production':
            self.app.logger.removeHandler(default_handler)
            self.app.logger.setLevel(logging.DEBUG)
            self.app.logger.addHandler(handler)
        
        self._misc_init()
        self._auto_register_blueprints()

        CORS(self.app)

    def _get_config(self):
        """."""

        config: configparser.ConfigParser = configparser.ConfigParser()
        config.read(os.path.join(self.BASE_DIR, 'resources', f'{self.ENV.lower()}.ini'))
        
        return config

    def _get_logging_handler(self):
        """."""
        
        log_format: str = '%(asctime)s  %(levelname)s  %(process)d  %(pathname)s  %(funcName)s  %(lineno)d  %(message)s'

        log_dir: str = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file: str = os.path.join(log_dir, 'debug.log')
        
        handler_options: dict = {
            'when': 'midnight',
            'interval': 1
        }
        
        handler: TimedRotatingFileHandler = TimedRotatingFileHandler(log_file, **handler_options)
        handler.setFormatter(logging.Formatter(log_format))
        
        return handler

    def _misc_init(self):
        """."""

        db.init_app(self.app)
        ma.init_app(self.app)
        migrate.init_app(self.app, db)

        with self.app.app_context():
            db.create_all()

    def _auto_register_blueprints(self):
        """."""

        for url_prefix, blueprint in url_prefix_x_blueprint.items():
            self.app.register_blueprint(blueprint, url_prefix=url_prefix)
    
    @classmethod
    def get_instance(cls, name: str) -> Flask:
        """."""

        if not cls.INSTANCE:
            cls.INSTANCE: Application = Application(name)
        
        return cls.INSTANCE.app
