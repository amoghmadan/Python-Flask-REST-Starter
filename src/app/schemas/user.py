from marshmallow import fields

from app.ext import ma
from app.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    """Schema: User"""

    email = fields.Email(required=True)

    class Meta:
        model = User
        load_instance = True
        load_only = ["password"]
