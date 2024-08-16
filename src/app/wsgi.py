from flask import Flask

from app import settings
from app.cli import manage
from app.ext import db, ma, migrate
from app.urls import urlpatterns


def get_wsgi_application():
    """
    Get WSGI Application, to return WSGI consumable Flask app.
    """
    app = Flask(__name__)
    app.config.update(
        DEBUG=settings.DEBUG,
        SECRET_KEY=settings.SECRET_KEY,
        SQLALCHEMY_DATABASE_URI=settings.SQLALCHEMY_DATABASE_URI,
    )
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db, directory=settings.BASE_DIR / __package__ / "migrations")

    app.register_blueprint(manage)
    for path, blueprint in urlpatterns:
        app.register_blueprint(blueprint, url_prefix=path)

    return app


application = get_wsgi_application()
