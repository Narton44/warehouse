from django.db import models

class Price(models.Model):
    
    price = models.FloatField(
        max_length=30,
        default=0.0,
    )

    p_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'цена'

        