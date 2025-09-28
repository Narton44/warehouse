from django.db import models
from models import StockIn, Product, Quantity, Price


class StockInItem(models.Model): # сам перечень товаров, указанный в документе проихода StockIn
    
    stockin = models.ForeignKey(
        StockIn,
        on_delete=models.CASCADE,
        ), 
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        ), 
    quantity = models.ForeignKey(
        Quantity,
        on_delete=models.CASCADE,
        ), 
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        ),

    def __str__(self):
        return f'text-text'
    
    class Meta:
        verbose_name = 'перечень'
        verbose_name_plural = 'перечни'