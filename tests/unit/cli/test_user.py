from click.testing import CliRunner

from app.ext import db
from app.models import User
from tests.base import TestCase


class TestUser(TestCase):
    """Test: User"""

    kwargs = {
        "email": "test.user.cli@foo.com",
        "first_name": "Foo",
        "last_name": "Bar",
    }
    password = "bar"

    def tearDown(self):
        user = User.query.filter_by(email=self.kwargs["email"]).first()
        if user is not None:
            db.session.delete(user)
            db.session.commit()
        super().tearDown()

    def test_createsuperuser_error(self):
        runner = CliRunner()
        manage = self.ctx.app.cli.commands["manage"]
        createsuperuser = manage.commands["createsuperuser"]
        input_for_prompts = [
            "not_an_email",
            self.kwargs["first_name"],
            self.kwargs["last_name"],
            self.password,
            self.password,
        ]
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(createsuperuser, input=test_input)
        user = User.query.filter_by(email=self.kwargs["email"]).first()
        assert user is None

    def test_createsuperuser_password_matching_error(self):
        runner = CliRunner()
        manage = self.ctx.app.cli.commands["manage"]
        createsuperuser = manage.commands["createsuperuser"]
        input_for_prompts = [
            "not_an_email",
            self.kwargs["first_name"],
            self.kwargs["last_name"],
            self.password,
            "baz",
        ]
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(createsuperuser, input=test_input)
        user = User.query.filter_by(email=self.kwargs["email"]).first()
        assert user is None

    def test_createsuperuser_duplicate(self):
        runner = CliRunner()
        manage = self.ctx.app.cli.commands["manage"]
        createsuperuser = manage.commands["createsuperuser"]
        input_for_prompts = [
            self.kwargs["email"],
            self.kwargs["first_name"],
            self.kwargs["last_name"],
            self.password,
            self.password,
        ]
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(createsuperuser, input=test_input)
        runner.invoke(createsuperuser, input=test_input)
        count = User.query.filter_by(email=self.kwargs["email"]).count()
        assert count == 1

    def test_createsuperuser_success(self):
        runner = CliRunner()
        manage = self.ctx.app.cli.commands["manage"]
        createsuperuser = manage.commands["createsuperuser"]
        input_for_prompts = [
            self.kwargs["email"],
            self.kwargs["first_name"],
            self.kwargs["last_name"],
            self.password,
            self.password,
        ]
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(createsuperuser, input=test_input)
        user = User.query.filter_by(email=self.kwargs["email"]).first()
        assert user is not None

    def test_changepassword_error(self):
        runner = CliRunner()
        manage = self.ctx.app.cli.commands["manage"]
        createsuperuser = manage.commands["createsuperuser"]
        input_for_prompts = [
            self.kwargs["email"],
            self.kwargs["first_name"],
            self.kwargs["last_name"],
            self.password,
            self.password,
        ]
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(createsuperuser, input=test_input)
        changepassword = manage.commands["changepassword"]
        input_for_prompts = ["baz"] * 2
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(changepassword, ["not_an_email"], input=test_input)
        user = User.query.filter_by(email=self.kwargs["email"]).first()
        assert user is not None
        assert user.check_password(input_for_prompts[0]) is False

    def test_changepassword_password_matching_error(self):
        runner = CliRunner()
        manage = self.ctx.app.cli.commands["manage"]
        createsuperuser = manage.commands["createsuperuser"]
        input_for_prompts = [
            self.kwargs["email"],
            self.kwargs["first_name"],
            self.kwargs["last_name"],
            self.password,
            self.password,
        ]
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(createsuperuser, input=test_input)
        created_user = User.query.filter_by(email=self.kwargs["email"]).first()
        assert created_user is not None
        changepassword = manage.commands["changepassword"]
        input_for_prompts = ["baz", "qux"]
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(changepassword, [self.kwargs["email"]], input=test_input)
        updated_user = User.query.filter_by(email=self.kwargs["email"]).first()
        assert updated_user is not None
        assert created_user.password == updated_user.password

    def test_changepassword_success(self):
        runner = CliRunner()
        manage = self.ctx.app.cli.commands["manage"]
        createsuperuser = manage.commands["createsuperuser"]
        input_for_prompts = [
            self.kwargs["email"],
            self.kwargs["first_name"],
            self.kwargs["last_name"],
            self.password,
            self.password,
        ]
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(createsuperuser, input=test_input)
        changepassword = manage.commands["changepassword"]
        input_for_prompts = ["baz"] * 2
        test_input = "\n".join(input_for_prompts) + "\n"
        runner.invoke(changepassword, [self.kwargs["email"]], input=test_input)
        user = User.query.filter_by(email=self.kwargs["email"]).first()
        assert user is not None
        assert user.check_password(input_for_prompts[0]) is True
