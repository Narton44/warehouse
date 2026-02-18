from django.views.generic import CreateView
from store.models import Product
from django.urls import reverse_lazy
from store.forms import ProductCreationForm

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'store/productadd.html'
    success_url = reverse_lazy('productlist')

    def form_valid(self,form):
        return super().form_valid(form)