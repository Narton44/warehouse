from django.db import models
from .supplier import Supplier
from .owncompany import OwnCompany


class StockIn(models.Model): 
    """документ прихода товаров на склад, без перечня товаров"""

    in_waybill_number = models.SlugField( # номер входящей накладной
        verbose_name='№ накладной',
        max_length=15,
        default='',
    ) 

    in_invoice_number = models.SlugField( # номер входящего счёта-фактуры
        verbose_name='№ счёта-фактуры',
        max_length=15,
        default='',
    ) 

    in_waybill_date = models.DateField( # дата входящего документа (не должна отличаться от даты счёта-фактуры более чем на 5 дней)
        verbose_name='Дата документа',
    )

    in_date = models.DateField( # дата оприходования
        verbose_name='Дата',
        help_text='текущая дата оприходования'
    )

    supplier = models.ForeignKey( # поставщик
        Supplier,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Поставщик',
    )

    buyer = models.ForeignKey( # покупатель (одна из наших фирм по которой ведется учёт)
        OwnCompany,
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='Покупатель',
    ) 

    is_posted = models.BooleanField( # статус документа(проведен/не проведён)
        default=False,
        verbose_name="Проведён",
    )

    comment = models.CharField( # произвольный комментарий
        max_length=50,
        verbose_name='Комментарий',
        default='',
    )

    def __str__(self):
        return f'{self.in_waybill_number} от {self.in_date}, ({self.supplier})'

    class Meta:
        verbose_name = 'поступление'
        verbose_name_plural = 'поступления'
        ordering = ['-in_date']