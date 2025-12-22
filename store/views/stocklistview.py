from django.views.generic import ListView
from store.models import Stock

class StockListView(ListView):
    model = Stock
    template_name = 'store/stock_list.html'
    context_object_name = 'stock_list'