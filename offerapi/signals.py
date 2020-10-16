import logging
import os
import requests

from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import Product

LOGGER = logging.getLogger('testlogger')
BASE_URL = os.environ.get('AL_BASE_URL')
BEARER_TOKEN = os.environ.get('AL_TOKEN')


@receiver(post_save, sender=Product)
def register_product(sender, instance, created, **kwargs):
    """
    Every time a product is created, register it to the AppLifting Product database.
    :param sender: Always Product in this case.
    :param instance: Instance of the freshly created Product
    :param created: True if created, false if updated
    """

    url = '{0}/products/register'.format(BASE_URL)
    headers = {
        'bearer': BEARER_TOKEN,
    }
    data = {
        'id': instance.id,
        'name': instance.name,
        'description': instance.description
    }
    """
    Register only when on production (testing data should not be registered through external API)
    and the product has been created, not updated
    """
    if not os.environ.get('DJANGO_DEBUG') and created:
        response = requests.post(url, headers=headers, data=data)
        LOGGER.info("Product registered: {0}".format(response.json()))
