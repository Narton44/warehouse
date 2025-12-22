from django.views.generic import CreateView
from store.models import Stock
from django.urls import reverse_lazy
from store.forms import StockCreationForm

class StockCreateView(CreateView):
    model = Stock
    form_class = StockCreationForm
    template_name = 'store/stockadd.html'
    success_url = reverse_lazy('stocklist')

    def form_valid(self,form):
        return super().form_valid(form)