from flask import Blueprint

from app.urls.api.v1.accounts import accounts

urlpatterns = [
    ("/accounts", accounts),
]

v1 = Blueprint("accounts", __name__)
for path, blueprint in urlpatterns:
    v1.register_blueprint(blueprint, url_prefix=path)

__all__ = ["v1"]
