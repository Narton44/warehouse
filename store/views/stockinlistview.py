from django.views.generic import ListView
from store.models import StockIn

class StockInListView(ListView):
    model = StockIn
    template_name = 'store/stockin_list.html'
    context_object_name = 'stockin'