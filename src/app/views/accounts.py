from datetime import datetime
from http import HTTPStatus

from flask import Response, jsonify, request, views
from marshmallow.exceptions import ValidationError

from app.ext import db
from app.models import Token, User
from app.schemas import TokenSchema, UserSchema
from app.utils.decorators import TokenAuthentication


class LoginView(views.MethodView):
    """Login View"""

    model = Token
    schema_class = TokenSchema

    def post(self, *args, **kwargs):
        """Login
        ---
        post:
          requestBody:
            content:
              application/json:
                schema: Token
          responses:
            201:
              description: Login success
              content:
                application/json:
                  schema: Token
        """
        if request.headers.get("Authorization"):
            return jsonify({"token": "Invalid token."}), HTTPStatus.BAD_REQUEST
        schema = self.schema_class()
        try:
            validated_data = schema.load(data=request.json)
        except ValidationError as e:
            return jsonify(e.messages), HTTPStatus.BAD_REQUEST
        user = User.query.filter_by(email=validated_data["email"]).first()
        if not user:
            return jsonify({"detail": "Invalid credentials."}), HTTPStatus.UNAUTHORIZED
        if not user.check_password(validated_data["password"]):
            return jsonify({"detail": "Invalid credentials."}), HTTPStatus.UNAUTHORIZED
        token = self.model.query.filter_by(user_id=user.id).first()
        if not token:
            token = self.model(user_id=user.id)
            db.session.add(token)
            user.last_login = datetime.now()
            db.session.commit()
        return jsonify(schema.dump({"token": token.key})), HTTPStatus.CREATED


class DetailView(views.MethodView):
    """Detail View"""

    decorators = [TokenAuthentication()]
    schema_class = UserSchema

    def get(self, *args, **kwargs):
        """Account detail
        ---
        get:
          responses:
            200:
              description: Account details
              content:
                application/json:
                  schema: User
        """
        schema = self.schema_class()
        return jsonify(schema.dump(request.user)), HTTPStatus.OK


class LogoutView(views.MethodView):
    """Logout View"""

    decorators = [TokenAuthentication()]
    model = Token

    def delete(self, *args, **kwargs):
        """Logout
        ---
        delete:
          responses:
            204:
              description: Logout successful
              content:
                application/json:
                  schema: User
        """
        obj = self.model.query.filter_by(user_id=request.user.id).first()
        db.session.delete(obj)
        db.session.commit()
        return Response(status=HTTPStatus.NO_CONTENT)
