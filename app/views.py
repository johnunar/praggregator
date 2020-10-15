from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from app.models import Product, Offer
from praggregator.serializers import ProductSerializer, UserSerializer, OfferSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows Templates to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OfferViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        API endpoint that allows Offers to be viewed.
        Other operations are disabled, as this app is not the source of offer objects.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
