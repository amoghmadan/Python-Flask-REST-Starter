from marshmallow import fields

from models import Person
from application.serializers import ma


class PersonSerializer(ma.SQLAlchemyAutoSchema):
    """."""

    name = fields.Str(required=True)
    age = fields.Int(required=True)

    class Meta:
        """."""

        model = Person
        load_instance = True
