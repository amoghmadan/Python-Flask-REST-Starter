from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db: SQLAlchemy = SQLAlchemy()
ma: Marshmallow = Marshmallow()
