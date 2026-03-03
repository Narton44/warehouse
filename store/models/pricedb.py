from django.db import models
from store.models import Product
from simple_history.models import HistoricalRecords

class PriceHistoryDB(models.Model): # класс истории изменения цен

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='prod'
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

    quantity = models.DecimalField(
        'количество',
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    history = HistoricalRecords()

    date = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'цены'
        ordering = ['date']