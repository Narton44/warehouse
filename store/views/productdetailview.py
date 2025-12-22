from django.views.generic import DetailView
from store.models import Product
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail_view.html'
    context_object_name = 'product'