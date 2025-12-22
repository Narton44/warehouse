from django.views.generic import DetailView
from store.models import Stock
from store.models import Product

class StockDetailView(DetailView):
    model = Stock
    template_name = 'store/stock_detail.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_product_list'] = Product.objects.filter(stock=self.object)
        return context