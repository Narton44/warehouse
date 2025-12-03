from django.db import models


class Bank(models.Model):

    name = models.CharField(
        verbose_name='банк',
        max_length=50,
        unique=True,
    )

    adress = models.CharField(
        verbose_name='адрес',
        max_length=100,
        unique=True,
    )

    phone_number = models.CharField(
        verbose_name='тел.',
        max_length=15,
    )

    email = models.EmailField(
        max_length=30,
        verbose_name='эл. почта',
        blank=True, null=True,
    )

    bank_id = models.CharField(
        verbose_name='БИК',
        max_length=9,
    )

    inn = models.CharField(
        verbose_name='ИНН',
    )

    ogrn = models.CharField(
        verbose_name='ОГРН',
        unique=True,
    )

    c_a = models.CharField(
        verbose_name='К/С',
        max_length=20,
        default=''
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'банк'
        verbose_name_plural = 'банки'
        ordering = ['name']