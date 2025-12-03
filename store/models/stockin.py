from django.db import models
from .supplier import Supplier
from .owncompany import OwnCompany


class StockIn(models.Model): # документ прихода товаров на склад, без перечня товаров

    waybill_number = models.SlugField(
        verbose_name='№ накладной',
        max_length=15,
        default='',
    )

    invoice_number = models.SlugField(
        verbose_name='№ счёта-фактуры',
        max_length=15,
        default='',
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

    stock_in_total = models.IntegerField(
        verbose_name='Сумма документа',
        default=0,
    )

    comment = models.CharField(
        max_length=50,
        verbose_name='Комментарий',
        default='',
    )


    def __str__(self):
        return f'{self.number} от {self.in_date}, ({self.supplier})'
    
    class Meta:
        verbose_name = 'поступление'
        verbose_name_plural = 'поступления'
        ordering = ['-in_date']