from app.ext import db
from app.models import User
from app.schemas import UserSchema
from tests.base import TestCase


class TestUserSchema(TestCase):
    """Test: User Schema"""

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

    def test_response_validation_success(self):
        schema = UserSchema()
        validated_data = schema.dump(self.user)
        assert len(validated_data.keys()) == 8
