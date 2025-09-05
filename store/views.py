from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Stock, Product

class StockListView(ListView):
    model = Stock
    template_name = 'store/index.html'
    context_object_name = 'stock_list'

