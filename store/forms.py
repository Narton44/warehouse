from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Stock, StockIn, StockOut, Product

class StockCreationForm(forms.ModelForm):
    
    class Meta:
        model = Stock
        fields = ['name', 'owner', 'adress']