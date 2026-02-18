from django.views.generic import ListView
from store.models import Product
from datetime import date 

class Index(ListView):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prod_num'] = Product.objects.all().count()
        context['today'] = date.today()
        return context