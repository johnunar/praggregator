import logging
import os
from json import JSONDecodeError

import requests

from app.models import Product

BASE_URL = os.environ.get('AL_BASE_URL')
BEARER_TOKEN = os.environ.get('AL_TOKEN')
LOGGER = logging.getLogger('console')


def get_offers(product):
    """
    Get a product's offers from the AppLifting Offer database.
    :param product: Product object for which are downloaded the offers
    :return: json-formatted offers
    """

    url = "{0}/products/{1}/offers/".format(BASE_URL, product.id)
    headers = {
        "bearer": BEARER_TOKEN,
    }

    response = requests.get(url=url, headers=headers)
    try:
        return response.json()
    except JSONDecodeError:
        return None


def update_product():
    """
    Function used to update products' offers. Reasonably fast for a small amount of data.
    At least a caching algorithm should be used for a larger product/offer database.
    """
    for product in Product.objects.all():
        offers = get_offers(product)
        if offers is not None:
            product.update_product_offers(get_offers(product))

    LOGGER.info("All products have been updated ({0})".format(Product.objects.all().count()))