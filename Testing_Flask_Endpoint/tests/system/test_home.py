from Automated_Testing.Testing_Flask_Endpoint.tests.system.base_test import BaseTest
from unittest import TestCase
import json


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.json, {'message': 'Hello, world!'})
