from django.views.generic import ListView
from store.models import Supplier

class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier_list'