from django.db import models
from .stockin import StockIn
from .product import Product
from simple_history.models import HistoricalRecords
from django.core.validators import MinValueValidator


class StockInProductItem(models.Model): # модель позиции (строка) товаров, указанный в документе проихода StockIn
    

    stockin = models.ForeignKey( # много строк у одной приходной накладной
        StockIn,
        related_name='stock_in_position',
        on_delete=models.CASCADE,
        ),
    
    product = models.ForeignKey( # много строк прихода у одного наименования товара
        Product,
        on_delete=models.PROTECT,
        related_name='product_item',
        verbose_name='Товар'
        ),
    
    quantity = models.DecimalField( # количество товара в приходе
        'количество',
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
    )

    purchase_price = models.DecimalField( # закупочная цена
        'закупочеая цена',
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
    )

    wholesale_price = models.DecimalField( # оптовая цена
        'оптовая цена',
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
    )

    retail_price = models.DecimalField( # розничная цена
        'розничная цена',
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
    )

    history = HistoricalRecords() # история изменения значений полей

    @property
    def amount(self):
        return self.quantity * self.retail_price
        
    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'позиция прихода'
        verbose_name_plural = 'позиции прихода'