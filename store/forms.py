# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from . models import StockIn, StockOut, Product

# class CtockInCreationForm(forms.ModelForm):
#     class Meta:
#         model = StockIn
#         fields = ['number', 'in_date', 'supplier', 'buyer', 'product',]
#         widgets = {
#             'number': forms.NumberInput(attrs={
#                 'class': 'form-control',
#                 'min': '0.01',
#                 'step': '0.01',
#                 'id': 'quantity-input'
#             }),
#             'in_date': forms.DateTimeInput(attrs={
#                 'class': 'form-control',
#                 'type': 'datetime-local'
#             }),
#             'supplier': forms.Select(attrs={
#                 'supplier': 'form-control select 2'
#             }),
#             'buyer': forms.Select(attrs={
#                 'uyer': 'form-control select 2'
#             }),
#             'product': forms.Select(attrs={
#                 'product': 'form-control select 2'
#             }),
#         }