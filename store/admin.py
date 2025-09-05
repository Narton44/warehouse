from django.contrib import admin
from .models import Stock, Product


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['name','adress',]
    list_filter = ['name','adress',]
    search_fields = ['name','adress',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','stock','id','price',]
    list_filter = ['name','stock','id','price',]
    search_fields = ['name','stock','id','price',]