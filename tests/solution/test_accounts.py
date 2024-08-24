from http import HTTPStatus
import json

from app.models import Token, User
from app.ext import db

from tests.base import TestCase

ROOT_URL = "/api/v1/accounts"


class TestAccountLoginAPI(TestCase):
    """Test Account API"""

    email = "test.login@foo.com"
    password = "bar"

    def setUp(self):
        self.user = User(
            email=self.email,
            first_name="Foo",
            last_name="Bar",
        )
        self.user.set_password(self.password)
        db.session.add(self.user)
        db.session.commit()
        self.headers = {"Content-Type": "application/json"}

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()

    def test_login_missing_credentials(self):
        data = json.dumps({"email": self.email})
        response = self.client.post(
            f"{ROOT_URL}/login", data=data, headers=self.headers
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_bad__request(self):
        data = json.dumps({"email": self.email, "password": self.password})
        headers = {"Content-Type": "application/json", "Authorization": "Token foo"}
        response = self.client.post(f"{ROOT_URL}/login", data=data, headers=headers)
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_login_bad_credentials(self):
        data = json.dumps({"email": self.email, "password": "foo"})
        response = self.client.post(
            f"{ROOT_URL}/login", data=data, headers=self.headers
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED

    def test_login(self):
        data = json.dumps({"email": self.email, "password": self.password})
        response = self.client.post(
            f"{ROOT_URL}/login", data=data, headers=self.headers
        )
        assert response.status_code == HTTPStatus.CREATED


class TestAccountAuthAPI(TestCase):
    """Test Account API"""

    email = "test.account@foo.com"
    password = "password"

    def setUp(self):
        user = User(
            email=self.email,
            first_name="Foo",
            last_name="Bar",
        )
        user.set_password(self.password)
        db.session.add(user)
        self.user = User.query.filter_by(email=self.email).first()
        db.session.commit()
        token = Token(user_id=self.user.id)
        db.session.add(token)
        db.session.commit()
        self.token = Token.query.filter_by(user_id=self.user.id).first()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {self.token.key}",
        }

    def tearDown(self):
        token = Token.query.filter_by(user_id=self.user.id).first()
        if token:
            db.session.delete(token)
        db.session.delete(self.user)
        db.session.commit()

    def test_no_auth_headers(self):
        headers = {"Content-Type": "application/json"}
        response = self.client.get(f"{ROOT_URL}/detail", headers=headers)
        assert response.status_code == HTTPStatus.UNAUTHORIZED

    def test_bad_keyword(self):
        headers = {"Content-Type": "application/json", "Authorization": "Random foo"}
        response = self.client.get(f"{ROOT_URL}/detail", headers=headers)
        assert response.status_code == HTTPStatus.UNAUTHORIZED

    def test_bad_auth_headers(self):
        headers = {"Content-Type": "application/json", "Authorization": "Token foo"}
        response = self.client.get(f"{ROOT_URL}/detail", headers=headers)
        assert response.status_code == HTTPStatus.UNAUTHORIZED

    def test_detail(self):
        response = self.client.get(f"{ROOT_URL}/detail", headers=self.headers)
        assert response.status_code == HTTPStatus.OK

    def test_logout(self):
        response = self.client.delete(f"{ROOT_URL}/logout", headers=self.headers)
        assert response.status_code == HTTPStatus.NO_CONTENT
