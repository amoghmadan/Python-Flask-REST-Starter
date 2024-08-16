import binascii
import os

from sqlalchemy.sql import func

from app.ext import db


def generate_key():
    """Generate a completely random string"""
    return binascii.hexlify(os.urandom(20)).decode()


class Token(db.Model):
    """Model: Token"""

    key = db.Column(db.String(40), default=generate_key, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return "<%s %r>" % (self.__class__.__name__, self.key)
