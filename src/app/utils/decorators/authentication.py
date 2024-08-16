from functools import wraps
from http import HTTPStatus

from flask import abort, jsonify, make_response, request

from app.models import Token, User


class TokenAuthentication:
    """Authentication: Token"""

    keyword = "Token"
    model = User

    def __call__(self, get_response):
        @wraps(get_response)
        def authenticate(*args, **kwargs):
            authorization = request.headers.get("Authorization")
            try:
                if authorization is None:
                    raise ValueError("Invalid authorization.")
                keyword, token = authorization.split()
                if keyword.title() != self.keyword:
                    raise ValueError("Invalid keyword.")
                token = Token.query.filter_by(key=token).first()
                if token is None:
                    raise ValueError("Invalid token.")
                current_user = self.model.query.filter_by(id=token.user_id).first()
                if current_user is None:
                    raise ValueError("Invalid token.")
                setattr(request, "user", current_user)
            except (AttributeError, ValueError):
                abort(
                    make_response(
                        jsonify({"detail": HTTPStatus.UNAUTHORIZED.phrase}),
                        HTTPStatus.UNAUTHORIZED,
                    )
                )
            return get_response(*args, **kwargs)

        return authenticate
