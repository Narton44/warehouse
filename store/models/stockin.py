from django.db import models
from .supplier import Supplier
from .owncompany import OwnCompany


class StockIn(models.Model): 
    """документ прихода товаров на склад, без перечня товаров"""

    in_waybill_number = models.SlugField(
        verbose_name='№ накладной',
        max_length=15,
        default='',
    ) # номер входящей накладной

    in_invoice_number = models.SlugField(
        verbose_name='№ счёта-фактуры',
        max_length=15,
        default='',
    ) # номер входящего счёта-фактуры

    in_date = models.DateField(
        verbose_name='Дата документа',
        auto_now_add=True,
    )# дата входящего документа

    supplier = models.ForeignKey(
        Supplier,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Поставщик',
    )# поставщик

    buyer = models.ForeignKey(
        OwnCompany,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Покупатель',
    ) # покупатель (одна из наших фирм по которой ведется учёт)

    is_posted = models.BooleanField(
        default=False,
        verbose_name="Проведён",
    ) # статус документа(проведен/не проведён)

    created_at = models.DateTimeField(auto_now_add=True) # момент создания документа

    updated_at = models.DateTimeField(auto_now=True) # момент создания документа

    comment = models.CharField(
        max_length=50,
        verbose_name='Комментарий',
        default='',
    ) # произвольный комментарий

    def __str__(self):
        return f'{self.in_waybill_number} от {self.in_date}, ({self.supplier})'

    class Meta:
        verbose_name = 'поступление'
        verbose_name_plural = 'поступления'
        ordering = ['-in_date']