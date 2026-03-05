from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Stock, StockIn, Bank, Product, OwnCompany, Supplier, Buyer, StockInProductItem
from django.forms import inlineformset_factory



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

class StockInProductItemForm(forms.ModelForm): # форма строки приходного документа

    class Meta:

        model = StockInProductItem
        fields = [
            # 'product',
            'quantity',
            'purchase_price',
            'wholesale_price',
            'retail_price',
            ]
        widgets = {
            # 'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'wholesale_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'retail_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            }

StockInProductItemFormSet = inlineformset_factory( # набор форм для позиций
StockIn,  # родительская модель
StockInProductItem,  # дочерняя модель
form=StockInProductItemForm,
extra=3,  # количество пустых форм для добавления новых позиций
can_delete=True,  # возможность удаления существующих позиций
)

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