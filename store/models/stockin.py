from django.db import models
from .supplier import Supplier
from .owncompany import OwnCompany
from .product import Product


class StockIn(models.Model): # документ прихода товаров на склад, без перечня товаров

    number = models.SlugField(
        verbose_name='№',
        max_length=15,
    )

    in_date = models.DateTimeField(
        verbose_name='Дата и время поступления',
        auto_now_add=True,
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Поставщик',
    )

    buyer = models.ForeignKey(
        OwnCompany,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Покупатель',
    )

    def __str__(self):
        return f'{self.number} от {self.in_date}, ({self.supplier})'
    
    class Meta:
        verbose_name = 'поступление'
        verbose_name_plural = 'поступления'
        ordering = ['-in_date']