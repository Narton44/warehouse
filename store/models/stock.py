from django.db import models

class Stock(models.Model):
    """Модель складов нашего предприятия (автозапчасти, электрика, сантехника, хозтовары и т.д.)"""
    name = models.CharField(
        verbose_name='склад',
        unique=True,
        max_length=50,
        )
    
    owner = models.ForeignKey(
        'OwnCompany',
        on_delete = models.PROTECT,
        max_length=50,
        verbose_name='владелец склада',
        blank=False,
        ) 
    
    adress = models.CharField(
        verbose_name='адрес',
        max_length=100,
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'склады'
        ordering = ['name']