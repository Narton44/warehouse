from django.db import models
from .buyer import Buyer
from .owncompany import OwnCompany
from .product import Product

class StockOut(models.Model):

    number = models.SlugField(
        verbose_name='№',
        max_length=15,
    )

    out_date = models.DateTimeField(
        verbose_name='Дата и время отгрузки',
        auto_now_add=True,
    )

    supplier = models.ForeignKey(
        OwnCompany,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Поставщик',
    )

    buyer = models.ForeignKey(
        Buyer,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Покупатель',
    )

    product = models.ManyToManyField(
        Product,
        verbose_name='товары',
    )

    def __str__(self):
        return f'{self.number} от {self.out_date}, {self.buyer}'
    
    class Meta:
        verbose_name = 'отгрузка'
        verbose_name_plural = 'отгрузки'
        ordering = ['-out_date']