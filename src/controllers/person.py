from flask import jsonify, request, views
from marshmallow.exceptions import ValidationError

from models import Person
from serializers import PersonSerializer
from application.database import db


class PersonController(views.MethodView):
    """."""

    def get(self, *args, **kwargs):
        """."""

        queryset: Person = Person.query.all()
        serializer: list = PersonSerializer(many=True)
        return jsonify(serializer.dump(queryset)), 200

    def post(self, *args, **kwargs):
        """."""

        try:
            serializer: PersonSerializer = PersonSerializer()
            queryset: Person = serializer.load(request.json)
            db.session.add(queryset)
            db.session.commit()
        except ValidationError as e:
            return jsonify(e.messages), 400
        else:
            return jsonify(serializer.dump(queryset)), 200


class PersonIdController(views.MethodView):
    """."""

    def get(self, *args, **kwargs):
        """."""

        id = kwargs.get("id")
        queryset: Person = Person.query.get(id)
        serializer: PersonSerializer = PersonSerializer()
        return jsonify(serializer.dump(queryset)), 200

    def put(self, *args, **kwargs):
        """."""

        try:
            id = kwargs.get("id")
            queryset: Person = Person.query.get(id)
            serializer: PersonSerializer = PersonSerializer()
            serializer.load(request.json, instance=queryset, partial=True)
            db.session.commit()
        except ValidationError as e:
            return jsonify(e.messages), 400
        else:
            return jsonify(serializer.dump(queryset)), 200

    def delete(self, *args, **kwargs):
        """."""

        id = kwargs.get("id")
        serializer: PersonSerializer = PersonSerializer()
        queryset: Person = Person.query.get(id)
        Person.query.filter_by(id=id).delete()
        db.session.commit()

        return jsonify(serializer.dump(queryset)), 200
