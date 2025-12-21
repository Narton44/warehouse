from django.db import models
from .stockin import StockIn
from .product import Product

from django.core.validators import MinValueValidator


class StockInProductList(models.Model): 
    """ сам перечень (строка) товаров, указанный в документе проихода StockIn"""

    stockin = models.ForeignKey(
        StockIn,
        related_name='in_position',
        on_delete=models.CASCADE,
        ), # много строк у одной приходной накладной

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name='Товар'
        ), # много строк прихода у одного наименования товара

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        validators=[MinValueValidator(0)],
        verbose_name="Количество"
        ), # количество товара в приходе

    price = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена",
        ), # цена товара в приходной накладной

    @property
    def amount(self):
        return self.quantity * self.price
        
    def __str__(self):
        return f"{self.product}: {self.quantity} x {self.price}"

    class Meta:
        verbose_name = 'перечень поступления'
        verbose_name_plural = 'перечни поступления'