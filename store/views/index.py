from django.views.generic import TemplateView
from store.models import Product, Stock
from datetime import date 

class Index(TemplateView):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_num'] = Stock.objects.all().count()        
        context['prod_num'] = Product.objects.all().count()
        # context['prod_num_available'] = Product.objects.filter(quantity__  > 1).count() # тут будет подсчет количества единиц товаров в наличии

        context['today'] = date.today()
        return context