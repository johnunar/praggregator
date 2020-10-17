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
        if BEARER_TOKEN is not None:
            self.assertEqual(response.status_code, 200)  # PyTest: assert response.status_code == 200
        else:
            self.assertEqual(response.status_code, 200,
                             msg="THE AL_TOKEN environment variable is not set. Remote connection test will fail "
                                 "without a correct token.")
