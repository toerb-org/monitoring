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

    def test_teslamate(self):
        r = requests.get('https://teslamate.toerb.de/')
        self.assertFalse(r.ok)
        self.assertEqual(r.status_code, 404)

    def test_nextcloud(self):
        r = requests.get('https://cloud.toerb.de/')
        self.assertTrue(r.ok)

        r = requests.get('https://cloud.toerb.de/apps/dashboard/')
        self.assertFalse(r.ok)
        self.assertEqual(r.status_code, 401)

    def test_gitlab(self):
        r = requests.get('https://gitlab.toerb.de/')
        self.assertTrue(r.ok)

        r = requests.get('https://gitlab.toerb.de/toerb')
        self.assertIn('tobiasgross.eu', r.text)

    def test_static(self):
        r = requests.get('https://tobiasgross.eu/')
        self.assertTrue(r.ok)
        self.assertIn('tobiasgross.eu', r.text)

        r = requests.get('https://www.tobiasgross.eu/')
        self.assertTrue(r.ok)
        self.assertIn('tobiasgross.eu', r.text)

        r = requests.get('https://mariesalm.de/')
        self.assertTrue(r.ok)
        self.assertIn('mariesalm.de', r.text)

        r = requests.get('https://www.mariesalm.de/')
        self.assertTrue(r.ok)
        self.assertIn('mariesalm.de', r.text)

        r = requests.get('https://things.toerb.de/test.txt')
        self.assertTrue(r.ok)
        self.assertEqual(r.text, 'success')
