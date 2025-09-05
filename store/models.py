from django.db import models
import uuid

class Stock(models.Model):

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
        null=True,
        ) 
    
    adress = models.CharField(
        verbose_name='адрес',
        max_length=100,
        blank=True
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'склады'
        ordering = ['name']
 

class Product(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True,        
        )

    stock = models.ForeignKey(
        Stock,
        on_delete=models.PROTECT,
        null=True,
        blank=False
        )
    
    id = models.AutoField(
        primary_key=True,
        help_text='уникальный ID товара',
        )
    
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
        )
    
    measure_unit = models.ForeignKey(
        'MeasureUnit',
        on_delete=models.PROTECT,
        verbose_name='ед. изм.',
        null=True,
        )
    
    price = models.PositiveIntegerField(
        verbose_name='цена',
        )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']


class MeasureUnit(models.Model):

    name = models.CharField(
        max_length=10,
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'ед. изм.'
        ordering = ['name']

class OwnCompany(models.Model):

    name = models.CharField(
        verbose_name='название',
        max_length=50,
        unique=True,
        blank=False,
        null=True,
    )

    adress = models.CharField(
        verbose_name='адрес',
        max_length=100,
        unique=True,
        blank=False,
        null=True,
    )

    phone_number = models.CharField(
        verbose_name='тел.',
        max_length=15,
    )

    inn = models.IntegerField(
        verbose_name='ИНН',
        unique=True,
        blank=False,
        null=True,
    )

    ogrn = models.IntegerField(
        verbose_name='ОГРН',
        unique=True,
        blank=False,
        null=True,
    )

    bank = models.ForeignKey(
        'Bank',
        on_delete=models.DO_NOTHING,
        verbose_name='банк',
    )

    bank_account = models.IntegerField(
        verbose_name='счёт в банке',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'своя фирма'
        verbose_name_plural = 'свои фирмы'
        ordering = ['name'] 


class Supplier(models.Model):

    name = models.CharField(
        verbose_name='название',
        max_length=50,
        unique=True,
        blank=False,
        null=True,
    )

    adress = models.CharField(
        verbose_name='адрес',
        max_length=100,
        unique=True,
        blank=False,
        null=True,
    )

    phone_number = models.CharField(
        verbose_name='тел.',
        max_length=15,
    )

    inn = models.IntegerField(
        verbose_name='ИНН',
        blank=False,
        null=True,
    )

    ogrn = models.IntegerField(
        verbose_name='ОГРН',
        unique=True,
        blank=False,
        null=True,
    )

    bank = models.ForeignKey(
        'Bank',
        on_delete=models.DO_NOTHING,
        verbose_name='банк',
    )

    bank_account = models.IntegerField(
        verbose_name='счёт в банке',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
        ordering = ['name']   


class Buyer(models.Model):

    name = models.CharField(
        verbose_name='название',
        max_length=50,
        unique=True,
        blank=False,
        null=True,
    )

    adress = models.CharField(
        verbose_name='адрес',
        max_length=100,
        unique=True,
        blank=False,
        null=True,
    )

    phone_number = models.CharField(
        verbose_name='тел.',
        max_length=15,
    )

    inn = models.IntegerField(
        verbose_name='ИНН',
        unique=True,
        blank=False,
        null=True,
    )

    ogrn = models.IntegerField(
        verbose_name='ОГРН',
        unique=True,
        blank=False,
        null=True,
    )

    bank = models.ForeignKey(
        'Bank',
        on_delete=models.DO_NOTHING,
        verbose_name='банк',
    )

    bank_account = models.IntegerField(
        verbose_name='счёт в банке',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'покупатель'
        verbose_name_plural = 'покупатели'
        ordering = ['name'] 


class Bank(models.Model):

    name = models.CharField(
        verbose_name='банк',
        max_length=50,
        unique=True,
        blank=False,
        null=True,
    )

    adress = models.CharField(
        verbose_name='адрес',
        max_length=100,
        unique=True,
        blank=False,
        null=True,
    )

    phone_number = models.CharField(
        verbose_name='тел.',
        max_length=15,
    )

    bank_id = models.IntegerField(
        verbose_name='БИК',
    )

    inn = models.IntegerField(
        verbose_name='ИНН',
        blank=False,
        null=True,
    )

    ogrn = models.IntegerField(
        verbose_name='ОГРН',
        unique=True,
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'банк'
        verbose_name_plural = 'банки'
        ordering = ['name'] 

    
class StockIn(models.Model):

    number = models.SlugField(
        verbose_name='№',
        max_length=15,
    )

    in_date = models.DateTimeField(
        verbose_name='Дата и время поступления',
        auto_now_add=True,
        blank=False,
        null=True,
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete = models.DO_NOTHING,
        max_length=50,
        verbose_name='Поставщик',
        blank=False,
        null=True,
    )

    buyer = models.ForeignKey(
        OwnCompany,
        on_delete = models.DO_NOTHING,
        max_length=50,
        verbose_name='Покупатель',
        blank=False,
        null=True,
    )

    stock = models.ForeignKey(
        Stock,
        on_delete=models.DO_NOTHING,

    )

    product = models.ManyToManyField(
        Product,
        verbose_name='товары',
    )

    def __str__(self):
        return f'{self.number} от {self.in_date}, {self.supplier}'
    
    class Meta:
        verbose_name = 'поступление'
        verbose_name_plural = 'поступления'
        ordering = ['-in_date']


class StockOut(models.Model):

    number = models.SlugField(
        verbose_name='№',
        max_length=15,
    )

    out_date = models.DateTimeField(
        verbose_name='Дата и время отгрузки',
        auto_now_add=True,
        blank=False,
        null=True,
    )

    supplier = models.ForeignKey(
        OwnCompany,
        on_delete = models.DO_NOTHING,
        max_length=50,
        verbose_name='Поставщик',
        blank=False,
        null=True,
    )

    buyer = models.ForeignKey(
        Buyer,
        on_delete = models.DO_NOTHING,
        max_length=50,
        verbose_name='Покупатель',
        blank=False,
        null=True,
    )

    stock = models.ForeignKey(
        Stock,
        on_delete=models.DO_NOTHING,

    )

    product = models.ManyToManyField(
        Product,
        verbose_name='товары',
    )

    def __str__(self):
        return f'{self.number} от {self.out_date}, {self.buyer}'
    
    class Meta:
        verbose_name = 'отгрузка'
        verbose_name_plural = 'отгрузки'
        ordering = ['-out_date']





        