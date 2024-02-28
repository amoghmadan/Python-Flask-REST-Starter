from marshmallow import fields

from utils import ma


class TokenSchema(ma.Schema):
    """Token Schema"""

    email = fields.Email(load_only=True, required=True)
    password = fields.String(load_only=True, required=True)
    token = fields.String(dump_only=True)
