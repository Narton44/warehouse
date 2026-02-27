from django.db import models
from store.models import Product

class Price: # класс истории изменения цен

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
    )

    purchase_price = models.DecimalField(
        'закупочеая цена',
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
    )

    wholesale_price = models.DecimalField(
        'оптовая цена',
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
    )

    retail_price = models.DecimalField(
        'розничная цена',
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
    )

    date = models.DateField(
        auto_now_add=True,
    )