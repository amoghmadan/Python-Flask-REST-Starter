from flask import Blueprint

from .accounts import accounts

routes = [
    ("/accounts", accounts),
]

api = Blueprint("api", __name__)
for path, blueprint in routes:
    api.register_blueprint(blueprint, url_prefix=path)

__all__ = ["api"]
