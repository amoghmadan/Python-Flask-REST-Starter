from sqlalchemy.sql import func

from utils import db
from utils.token import generate_key


class Token(db.Model):
    """Token Model"""

    key = db.Column(db.String(40), default=generate_key, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return "<%s %r>" % (self.__class__.__name__, self.key)
