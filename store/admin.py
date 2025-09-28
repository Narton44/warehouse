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



class ProductInline(admin.TabularInline):
    model = Product
    extra =0

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'adress',]
    list_filter = ['name', 'owner', 'adress',]
    search_fields = ['name', 'owner', 'adress',]
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','stock','supplier_id', 'measure_unit',]
    list_filter = ['stock',]
    search_fields = ['stock__name','stock','supplier_id', 'measure_unit',]

admin.site.register(Bank)
admin.site.register(Buyer)
admin.site.register(OwnCompany)
admin.site.register(StockIn)
admin.site.register(StockOut)
admin.site.register(Supplier)