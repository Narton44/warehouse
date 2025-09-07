from django.contrib import admin
from .models import (
    Stock, 
    Product, 
    Bank,
    Buyer,
    OwnCompany,
    StockIn,
    StockOut,
    Supplier,
    )


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'adress',]
    list_filter = ['name', 'owner', 'adress',]
    search_fields = ['name', 'owner', 'adress',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','stock','id', 'quantity', 'measure_unit', 'price',]
    list_filter = ['name','stock','id', 'quantity', 'measure_unit', 'price',]
    search_fields = ['name','stock','id', 'quantity', 'measure_unit', 'price',]

admin.site.register(Bank)
admin.site.register(Buyer)
admin.site.register(OwnCompany)
admin.site.register(StockIn)
admin.site.register(StockOut)
admin.site.register(Supplier)