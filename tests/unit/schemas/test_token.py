from marshmallow.exceptions import ValidationError

from app.ext import db
from app.models import User, Token
from app.schemas import TokenSchema
from tests.base import TestCase


class TestTokenSchema(TestCase):
    """Test: Token Schema"""

    kwargs = {
        "email": "test.user.schema@foo.com",
        "first_name": "Foo",
        "last_name": "Bar",
    }
    password = "bar"

    def setUp(self):
        super().setUp()
        self.user = User(**self.kwargs)
        self.user.set_password(self.password)
        db.session.add(self.user)
        db.session.commit()
        db.session.refresh(self.user)

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()
        super().tearDown()

    def test_validation_error(self):
        payload = {"email": 1234, "password": self.password}
        schema = TokenSchema()
        with self.assertRaises(ValidationError):
            schema.load(data=payload)

    def test_validation_success(self):
        payload = {"email": self.kwargs["email"], "password": self.password}
        schema = TokenSchema()
        validated_data = schema.load(data=payload)
        assert len(validated_data.keys()) == 2

    def test_response_validation_error(self):
        schema = TokenSchema()
        validated_data = schema.dump({"random-key": "x" * 40})
        assert len(validated_data.keys()) == 0

    def test_response_validation_success(self):
        schema = TokenSchema()
        validated_data = schema.dump({"token": "x" * 40})
        assert len(validated_data.keys()) == 1
