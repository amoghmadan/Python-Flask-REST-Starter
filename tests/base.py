import unittest

from app.ext import db
from app.wsgi import application


class TestCase(unittest.TestCase):
    """Flask Test Case"""

    ctx = application.app_context()

    @classmethod
    def setUpClass(cls):
        cls.ctx.push()
        cls.client = application.test_client()
        with cls.ctx.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        cls.ctx.pop()
