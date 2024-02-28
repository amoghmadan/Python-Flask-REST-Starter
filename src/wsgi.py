from flask import Flask

from cli import manage
from routes import routes
from utils import db, ma
import settings


def get_wsgi_application():
    app = Flask(__name__)
    app.config.update(
        DEBUG=settings.DEBUG,
        SQLALCHEMY_DATABASE_URI=settings.SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=settings.SQLALCHEMY_TRACK_MODIFICATIONS,
    )
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(manage)
    for path, blueprint in routes:
        app.register_blueprint(blueprint, url_prefix=path)

    return app


application = get_wsgi_application()

if __name__ == "__main__":
    application.run()
