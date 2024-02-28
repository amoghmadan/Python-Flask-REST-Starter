from getpass import getpass

from flask import Blueprint
from marshmallow.exceptions import ValidationError
import click

from models import User
from schemas import UserSchema
from utils import db

manage = Blueprint("manage", __name__)


@manage.cli.command("changepassword")
@click.argument("email")
def changepassword(email):
    """Change password for the existing user in the application."""
    user = User.query.filter_by(email=email).first()
    if not user:
        raise Exception("User with this email does not exist.")
    password = getpass("Password: ")
    confirm_password = getpass("Confirm password: ")
    if password != confirm_password:
        raise Exception("Both the passwords should match.")
    try:
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
    except ValidationError as e:
        raise Exception(e.messages)


@manage.cli.command("createsuperuser")
def createsuperuser():
    """Create a user for the application."""
    email = input("Email: ")
    if User.query.filter_by(email=email).first():
        raise Exception("User with this email already exists.")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    password = getpass("Password: ")
    confirm_password = getpass("Confirm password: ")
    if password != confirm_password:
        raise Exception("Both the passwords should match.")
    data = {"email": email, "first_name": first_name, "last_name": last_name, "is_admin": True}
    schema = UserSchema()
    try:
        user = schema.load(data)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
    except ValidationError as e:
        raise Exception(e.messages)
