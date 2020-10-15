import json
import os
import unittest

import requests
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate


class LocalConnectionTest(TestCase):
    """
    Basic test to check if the API is available
    """

    def setUp(self):
        self.client = Client()

    def test_products(self):
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, 200)

    def test_offers(self):
        response = self.client.get('/api/v1/offers/')
        self.assertEqual(response.status_code, 200)


class ProductAPITest(TestCase):
    """
    Test to check if Product API works fine.
    """

    def setUp(self):
        self.client = Client()

        # These should work with post and update.
        self.valid_post_data = {
            "name": "Product Name",
            "description": "Product Description"
        }

        # These should not work with post and update
        self.invalid_post_data = {
            "name": "",
            "description": "Another Description"
        }

        # Generate a one-off testing superuser with a token. -> Authentication is tested, too.
        self.user = User.objects.create_superuser(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

    def test_crud_product(self):
        """
            Test for CRUD operations on a product objects
        """
        # CREATE
        post_response = self.client.post('/api/v1/products/', data=self.valid_post_data,
                                         HTTP_AUTHORIZATION='Token {0}'.format(self.token))
        self.assertEqual(post_response.status_code, 201)

        # READ
        get_response = self.client.get('/api/v1/products/{0}/'.format(post_response.json()['id']))
        self.assertEqual(get_response.status_code, 200)

        # UPDATE
        update_response = self.client.put('/api/v1/products/{0}/'.format(post_response.json()['id']),
                                          data=json.dumps(self.valid_post_data),
                                          content_type='application/json',
                                          HTTP_AUTHORIZATION='Token {0}'.format(self.token))
        self.assertEqual(update_response.status_code, 200)

        # DELETE
        delete_response = self.client.delete('/api/v1/products/{0}/'.format(post_response.json()['id']),
                                             HTTP_AUTHORIZATION='Token {0}'.format(self.token))
        self.assertEqual(delete_response.status_code, 204)

    def test_invalid_create_product(self):
        """
            Test if a product is NOT created when a required parameter is not provided
        """
        post_response = self.client.post('/api/v1/products/', data=self.invalid_post_data,
                                         HTTP_AUTHORIZATION='Token {0}'.format(self.token))

        self.assertNotEqual(post_response.status_code, 201)

    def test_invalid_update_product(self):
        """
            Test if a product is NOT updated when a required parameter is not provided
        """
        data = json.dumps(self.invalid_post_data)
        update_response = self.client.put('/api/v1/products/3/', data=data, content_type='application/json',
                                          HTTP_AUTHORIZATION='Token {0}'.format(self.token))

        self.assertNotEqual(update_response.status_code, 200)
