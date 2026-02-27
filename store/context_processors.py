from .models import Product, Stock
from django.db.models import Sum

def stock_summary(request):

    stock_count = Stock.objects.count() # Количество складов 
    total_units = Product.objects.aggregate(total=Sum('quantity'))['total'] or 0 # Общее количество товаров на всех складах
    product_count = Product.objects.values('name').distinct().count() # Количество уникальных товаров

    return {
        'total_stock_units': total_units,
        'total_stocks': stock_count,
        'unique_products': product_count,
    }
