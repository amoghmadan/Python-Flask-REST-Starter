import unittest

from wsgi import application


class TestCase(unittest.TestCase):
    """Flask Test Case"""

    ctx = application.app_context()

    @classmethod
    def setUpClass(cls):
        cls.ctx.push()
        cls.client = application.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.ctx.pop()
