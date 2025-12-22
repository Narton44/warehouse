from django.views.generic import ListView
from store.models import StockOut

class StockOutListView(ListView):
    model = StockOut
    template_name = 'store/stockout_list.html'
    context_object_name = 'stockout'