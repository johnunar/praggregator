from rest_framework import viewsets, mixins

from app.models import Product, Offer
from praggregator.serializers import ProductSerializer, OfferSerializer


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

    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Offer.objects.all()
        external_id = self.request.query_params.get("id", None)
        prices_from = self.request.query_params.get("pricesFrom", None)
        prices_to = self.request.query_params.get("pricesTo", None)

        if external_id is not None:
            queryset = queryset.filter(external_id=external_id)
        if prices_from is not None and prices_to is not None:
            for item in queryset:
                item.historical_prices = dict(
                    filter(lambda elem: prices_from <= elem[0] <= prices_to, item.historical_prices.items()))
                if len(item.historical_prices) != 0:
                    first_value = list(item.historical_prices.values())[0]
                    last_value = list(item.historical_prices.values())[-1]
                    delta = round(100 * (last_value - first_value) / first_value, 2)
                    if delta < 0:
                        item.delta = str(-delta) + " % fall"
                    elif delta > 0:
                        item.delta = str(delta) + " % rise"
                    else:
                        item.delta = str(delta) + " %"
                else:
                    item.delta = "No price logs found in the provided range"
        return queryset
