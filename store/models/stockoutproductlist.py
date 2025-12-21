from django.db import models
from .stockout import StockOut
from .product import Product

from django.core.validators import MinValueValidator



class StockOutProductList(models.Model): # сам перечень товаров, указанный в документе расхода StockOut
    """ сам перечень (строка) товаров, указанный в документе расода StockOut"""
    
    stockout = models.ForeignKey(
        StockOut,
        related_name='out_position',
        on_delete=models.CASCADE,
        ), # много строк у одной расходной накладной

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name='Товар'
        ), # много строк расхода у одного наименования товара 

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        validators=[MinValueValidator(0)],
        verbose_name="Количество"
        ), # количество товара в расходе 

    price = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена"
        ), # цена товара в расходной накладной

    def __str__(self):
        return f"{self.product}: {self.quantity} x {self.price}"
    
    class Meta:
        verbose_name = 'перечень отгрузки'
        verbose_name_plural = 'перечни отгрузки'