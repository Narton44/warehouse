from django.views.generic import CreateView
from django.urls import reverse_lazy
from store.models import StockIn
from store.forms import StockInCreationForm

class StockInCreateView(CreateView):
    model = StockIn
    form_class = StockInCreationForm
    template_name = 'store/stockinadd.html' # to create!!!
    success_url = reverse_lazy('stockin')

    def form_valid(self,form):
        return super().form_valid(form)