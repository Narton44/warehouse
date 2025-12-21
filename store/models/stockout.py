from django.db import models
from .buyer import Buyer
from .owncompany import OwnCompany

class StockOut(models.Model):
    """документ расхода товаров со склада, без перечня товаров"""
    out_waybill_number = models.SlugField(
        verbose_name='№ накладной',
        max_length=15,
        default='',
    ) # номер исходящей накладной

    out_invoice_number = models.SlugField(
        verbose_name='№ счёта-фактуры',
        max_length=15,
        default='',
    ) # номер исходящего счёта-фактуры

    out_date = models.DateField(
        verbose_name='Дата документа',
        auto_now_add=True,
    )# дата исходящего документа

    supplier = models.ForeignKey(
        OwnCompany,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Поставщик',
    ) # поставщик (одна из наших фирм по которой ведется учёт)

    buyer = models.ForeignKey(
        Buyer,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Покупатель',
    ) # покупатель

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
        return f'{self.out_waybill_number} от {self.out_date}, {self.buyer}'
    
    class Meta:
        verbose_name = 'отгрузка'
        verbose_name_plural = 'отгрузки'
        ordering = ['-out_date']