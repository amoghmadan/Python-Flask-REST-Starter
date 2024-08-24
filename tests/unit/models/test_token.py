from app.models import Token, User
from app.ext import db
from tests.base import TestCase


class TestUserModel(TestCase):
    """Test: User Model"""

    kwargs = {
        "email": "test.token@foo.com",
        "first_name": "Foo",
        "last_name": "Bar",
    }
    password = "bar"

    def test_repr(self):
        token = Token(user_id=1234)
        assert "<Token None>" == str(token)

    def test_password(self):
        # Create User and Token
        user = User(**self.kwargs)
        user.set_password(self.password)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        token = Token(user_id=user.id)
        db.session.add(token)
        db.session.commit()
        db.session.refresh(token)
        # Test
        assert len(token.key) == 40
        # Clean Up
        db.session.delete(token)
        db.session.delete(user)
        db.session.commit()
