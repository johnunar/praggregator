from django.db.models import CharField, IntegerField, ForeignKey, Model, CASCADE, PositiveIntegerField


class Product(Model):
    """
    Model representing a real-world product that is available to be bought.
    For example: AH-64 Apache Attack Helicopter
    """
    name = CharField(max_length=300)
    description = CharField(max_length=500)

    def __str__(self):
        return self.name

    def update_product_offers(self, offers):
        for remote_offer in offers:
            try:
                local_offer = Offer.objects.get(external_id=remote_offer['id'])
                local_offer.price = remote_offer['price']
                local_offer.items_in_stock = remote_offer['items_in_stock']
                local_offer.save()
            except Offer.DoesNotExist:
                Offer.objects.create(price=remote_offer['price'], items_in_stock=remote_offer['items_in_stock'],
                                     external_id=remote_offer['id'], product=self)


class Offer(Model):
    """
        Model representing a product offer being sold for some price in a shop.
        Data for this object are periodically synchronised with the AppLifting external offers database using REST API.
        For example: AH-64A Apache Attack Helicopter is being sold for $20 000 000 and they have 2 of them in stock
    """
    price = IntegerField()
    items_in_stock = IntegerField()
    external_id = PositiveIntegerField(unique=True)
    product = ForeignKey(
        Product,
        on_delete=CASCADE,
        related_name='products',
    )

    def __str__(self):
        return self.product.name + " (" + str(self.price) + ",-)"
