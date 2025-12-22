from django.views.generic import DetailView
from store.models import Supplier

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'store/supplier_detail_view.html'
    context_object_name = 'supplier'