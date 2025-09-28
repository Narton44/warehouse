from django.db import models
from .stock import Stock

class Product(models.Model):

    MEASURE_UNIT = [
        ("шт.", "шт."),
        ("кг.", "кг."),
        ("м.", "м."),
        ("кв.м.", "кв.м."),
        ("л.", "л."),
        ("уп.", "уп."),
        ("т.", "т."),
        ("куб.м.", "куб.м."),
    ]
    
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='наименование',      
        )

    stock = models.ForeignKey(
        Stock,
        on_delete=models.PROTECT,
        verbose_name='склад',
        )
    
    supplier_id = models.CharField(
        max_length=30,
        verbose_name='артикул',
        )
    
    measure_unit = models.CharField(
        choices=MEASURE_UNIT,
        verbose_name='ед.изм.',
        )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']