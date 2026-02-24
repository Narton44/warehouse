from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Stock, StockIn, Bank, Product, OwnCompany

class StockCreationForm(forms.ModelForm):
    
    class Meta:
        model = Stock
        fields = ['name', 'owner', 'adress']

class ProductCreationForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'stock', 'supplier_id', 'measure_unit',]

class StockInCreationForm(forms.ModelForm):

    class Meta:
        model = StockIn
        fields = [
            'in_waybill_number',
            'in_invoice_number',
            'in_waybill_date',
            'in_date',
            'supplier',
            'buyer',
            'is_posted',
            'comment',
        ]

class OwnCompanyCreationForm(forms.ModelForm):

    class Meta:
        model = OwnCompany
        fields = [
            'name',
            'adress',
            'phone_number',
            'email',
            'inn',
            'ogrn',
            'bank',
            'bank_account',
        ]

class BankCreationForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = [
            'name',
            'adress',
            'phone_number',
            'email',
            'bank_id',
            'inn',
            'ogrn',
            'c_a',
        ]