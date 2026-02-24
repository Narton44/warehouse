from django.views.generic import CreateView
from store.models import StockIn
from store.forms import StockInCreationForm
from django.urls import reverse_lazy

class StockInCreateView(CreateView):
    model = StockIn
    form_class = StockInCreationForm
    template_name = 'store/stockinadd.html'
    success_url = reverse_lazy('stockin')

    # def form_valid(self,form):
    #     return super().form_valid(form)