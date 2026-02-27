from django.views.generic import CreateView
from store.models import Buyer
from django.urls import reverse_lazy
from store.forms import BuyerCreationForm

class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerCreationForm
    template_name = 'store/buyeradd.html'
    success_url = reverse_lazy('buyerlist')

    def form_valid(self,form):
        return super().form_valid(form)