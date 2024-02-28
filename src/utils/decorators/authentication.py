from http import HTTPStatus
from functools import wraps

from flask import abort, jsonify, make_response, request

from models import Token, User


class TokenAuthentication:
    """Token Authentication"""

    keyword = "Token"
    model = User

    def __call__(self, get_response):
        @wraps(get_response)
        def authenticate(*args, **kwargs):
            authorization = request.headers.get("Authorization")
            try:
                keyword, token = authorization.split()
                assert keyword.title() == self.keyword, "Invalid keyword."
                token = Token.query.filter_by(key=token).first()
                assert token is not None, "Invalid token."
                current_user = self.model.query.filter_by(id=token.user_id).first()
                assert current_user is not None, "Invalid token."
                setattr(request, "user", current_user)
            except (AssertionError, AttributeError, ValueError):
                abort(
                    make_response(
                        jsonify({"detail": "Unauthorized"}),
                        HTTPStatus.UNAUTHORIZED,
                    )
                )
            return get_response(*args, **kwargs)

        return authenticate
