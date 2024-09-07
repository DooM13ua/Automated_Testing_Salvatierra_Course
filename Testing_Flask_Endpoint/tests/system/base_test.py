from unittest import TestCase
from Automated_Testing.Testing_Flask_Endpoint.app import app


class BaseTest(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client
