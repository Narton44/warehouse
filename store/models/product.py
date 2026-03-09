from django.db import models
from . import Stock
from simple_history.models import HistoricalRecords


class Product(models.Model): # Модель товара

    MEASURE_UNIT = [
        ("шт.", "шт."),
        ("кг.", "кг."),
        ("м.", "м."),
        ("кв.м.", "кв.м."),
        ("л.", "л."),
        ("уп.", "уп."),
        ("т.", "т."),
        ("куб.м.", "куб.м."),
        ("пог.м.", "пог.м."),
    ]

    name = models.CharField( # наименование товара
        max_length=50,
        unique=True,
        verbose_name='наименование',      
        )

    stock = models.ForeignKey(
        Stock,
        verbose_name='склад',
        on_delete=models.PROTECT,
        related_name='native_stock',
    )

    supplier_id = models.CharField( # артикул товара
        max_length=30,
        unique=True,
        primary_key=True,
        verbose_name='артикул',
        )

    measure_unit = models.CharField( # единица измерения товара
        choices=MEASURE_UNIT,
        verbose_name='ед.изм.',
        )

    VAT_tax = models.SmallIntegerField( # ставка НДС
        verbose_name='НДС',
        null=True,
        blank=True,
        )

    history = HistoricalRecords() # история изменения значений полей


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']