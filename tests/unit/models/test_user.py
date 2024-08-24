from app.models import User
from app.ext import db
from tests.base import TestCase


class TestUserModel(TestCase):
    """Test: User Model"""

    kwargs = {
        "email": "test.user@foo.com",
        "first_name": "Foo",
        "last_name": "Bar",
    }
    password = "bar"

    def test_repr(self):
        user = User(**self.kwargs)
        assert "<User None>" == str(user)

    def test_password(self):
        user = User(**self.kwargs)
        user.set_password(self.password)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        assert user.check_password(self.password) == True
        db.session.delete(user)
        db.session.commit()
