from django.contrib import admin

from app.models import Product, Offer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price', 'items_in_stock')
