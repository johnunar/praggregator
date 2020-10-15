import os
import unittest

import requests

BEARER_TOKEN = os.environ.get('AL_TOKEN')


class RemoteConnectionTest(unittest.TestCase):
    """
        Test the connection to the Offers server.
    """

    def test_offers_connection(self):
        base_url = os.environ.get('AL_BASE_URL')
        url = "{0}/products/1/offers".format(base_url)
        headers = {
            "bearer": BEARER_TOKEN,
        }

        response = requests.get(url=url, headers=headers)
        self.assertEqual(response.status_code, 200)  # PyTest: assert response.status_code == 200
