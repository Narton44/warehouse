from django.views.generic import CreateView
from store.models import Supplier
from django.urls import reverse_lazy
from store.forms import SupplierCreationForm

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierCreationForm
    template_name = 'store/supplieradd.html'
    success_url = reverse_lazy('supplierlist')

    def form_valid(self,form):
        return super().form_valid(form)