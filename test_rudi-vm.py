import unittest

import requests


class TestHTTPS(unittest.TestCase):
    def test_matrix(self):
        r = requests.get('https://element.toerb.de')
        self.assertTrue(r.ok)

        r = requests.get('https://toerb.de/.well-known/matrix/server')
        self.assertTrue(r.ok)
        self.assertEqual(r.json()['m.server'], 'matrix.toerb.de')

        r = requests.get('https://matrix.toerb.de:8448/_matrix/federation/v1/version')
        self.assertTrue(r.ok)
        self.assertIn('server', r.json())