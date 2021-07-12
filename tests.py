import pytest
from app_conf import create_app

import unittest

app = create_app()


class BasicTest(unittest.TestCase):

    def setUp(self):
        app.config['Testing'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()

    def test_distance(self):
        rv = self.app.get('/')
        print(rv.status_code)
        self.assertEqual(rv.status_code, 200)


if __name__ == "__main__":
    unittest.main()
