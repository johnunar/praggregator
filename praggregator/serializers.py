from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import CharField

from app.models import Offer, Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'description')


class OfferSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    delta = CharField()

    class Meta:
        model = Offer
        fields = ('id', 'price', 'items_in_stock', 'external_id', 'product', 'delta')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
