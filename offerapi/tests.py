import os

import requests
from django.test import TestCase

BASE_URL = os.environ.get('AL_BASE_URL')
BEARER_TOKEN = os.environ.get('AL_TOKEN')


class RemoteConnectionTest(TestCase):
    """
        Test the connection to the Offers server.
    """

    def test_offers_connection(self):
        url = "{0}/products/1/offers/".format(BASE_URL)
        headers = {
            "bearer": BEARER_TOKEN,
        }
        response = requests.get(url=url, headers=headers)
        self.assertEqual(response.status_code, 200)  # PyTest: assert response.status_code == 200
