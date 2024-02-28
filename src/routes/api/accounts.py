from flask import Blueprint

from views.accounts import DetailView, LoginView, LogoutView

accounts = Blueprint("account", __name__)
accounts.add_url_rule("/detail", view_func=DetailView.as_view("detail"), methods=["GET"])
accounts.add_url_rule("/login", view_func=LoginView.as_view("login"), methods=["POST"])
accounts.add_url_rule(
    "/logout", view_func=LogoutView.as_view("logout"), methods=["DELETE"]
)
