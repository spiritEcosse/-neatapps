__author__ = 'igor'
from django.test import TestCase
from django.test import Client


class NeatappsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_available_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
