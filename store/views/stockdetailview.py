from django.views.generic import DetailView
from store.models import Stock
from store.models import Product
from django.db.models import Sum


class StockDetailView(DetailView):
    model = Stock
    template_name = 'store/stock_detail.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_product_list'] = Product.objects.filter(stock=self.object) # фильтр товара на данном складе
        context['stock_product_list_count'] = Product.objects.filter(stock=self.object).count() # количество наименований товара на данном складе
        return context