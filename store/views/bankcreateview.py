from django.views.generic import CreateView
from store.models import Bank
from django.urls import reverse_lazy
from store.forms import BankCreationForm

class BankCreateView(CreateView):
    model = Bank
    form_class = BankCreationForm
    template_name = 'store/bankadd.html'
    success_url = reverse_lazy('banklist')

    def form_valid(self,form):
        return super().form_valid(form)