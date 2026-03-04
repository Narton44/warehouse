from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Stock, StockIn, Bank, Product, OwnCompany, Supplier, Buyer, StockInProductItem


class StockCreationForm(forms.ModelForm): # форма создания склада
    
    class Meta:
        model = Stock
        fields = ['name', 'owner', 'adress']

class ProductCreationForm(forms.ModelForm): # форма создания карточки товара

    class Meta:
        model = Product
        fields = ['name', 'stock', 'supplier_id', 'measure_unit', 'VAT_tax', 'customs_declaration',]

class StockInCreationForm(forms.ModelForm): # форма создания поступления товаров

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

class OwnCompanyCreationForm(forms.ModelForm): # форма создания своей фирмы

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

class BankCreationForm(forms.ModelForm): # форма создания банка

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

class SupplierCreationForm(forms.ModelForm): # форма создания поставщика

    class Meta:
        model = Supplier
        fields = [
            'name',
            'adress',
            'email',
            'phone_number',
            'inn',
            'ogrn',
            'bank',
            'bank_account',
        ]

class BuyerCreationForm(forms.ModelForm): # форма создания покупателя

    class Meta:
        model = Buyer
        fields = [
            'name',
            'adress',
            'email',
            'phone_number',
            'inn',
            'ogrn',
            'bank',
            'bank_account',
        ]