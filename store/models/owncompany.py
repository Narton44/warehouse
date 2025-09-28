from django.db import models


class OwnCompany(models.Model):

    name = models.CharField(
        verbose_name='название',
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

    inn = models.CharField(
        verbose_name='ИНН',
        unique=True,
    )

    ogrn = models.CharField(
        verbose_name='ОГРН',
        unique=True,
    )

    bank = models.ForeignKey(
        'Bank',
        on_delete=models.PROTECT,
        verbose_name='банк',
    )

    bank_account = models.CharField(
        verbose_name='счёт в банке',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'своя фирма'
        verbose_name_plural = 'свои фирмы'
        ordering = ['name']