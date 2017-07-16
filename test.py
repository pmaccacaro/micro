#!/usr/bin/env python
import unittest
import api
import requests


class TestCountriesTarget(unittest.TestCase):

    def test_source(self):
        print('Test Source API')
        response = requests.get(
            'http://localhost:8080/v1/countries?target=source')
        self.assertEqual(response.json(), [{u'isoCode': u'GB', u'name': u'United Kingdom'}, {
                         u'isoCode': u'IE', u'name': u'Ireland'}, {u'isoCode': u'IT', u'name': u'Italy'}])

    def test_destination(self):
        print('Test Destination API')
        response = requests.get(
            'http://localhost:8080/v1/countries?target=destination')
        self.assertEqual(response.json(), [{"name": "Spain", "isoCode": "ES"}, {
            "name": "France", "isoCode": "FR"}, {"name": "Germany", "isoCode": "DE"}])


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        print('Setup Test')
        self.app = api.app.test_client()

    def test_home_page(self):
        print('Home Page')
        response = self.app.get('/')

if __name__ == "__main__":
    unittest.main()
