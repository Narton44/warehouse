from django.views.generic import CreateView
from store.models import StockIn

class StockInCreateView(CreateView):
    model = StockIn
    form_class = StockInCreationForm # to create!!!
    template_name = 'store/stockinadd.html' # to create!!!
    success_url = reverse_lazy('stockin')

    def form_valid(self,form):
        return super().form_valid(form)