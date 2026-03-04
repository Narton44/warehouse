from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404
from store.models import StockIn, StockInProductItem
from store.forms import StockInCreationForm
from django.urls import reverse_lazy

class StockInCreateView(CreateView): #класс создания закупки товаров
    model = StockIn
    form_class = StockInCreationForm
    template_name = 'store/stockinadd.html'
    success_url = reverse_lazy('stockin')

    def form_valid(self,form):
        return super().form_valid(form)

    # def stockin_detail(request, pk):
    #     stockin = get_object_or_404(StockIn, pk=pk)
    #     products = stockin.product_set.all()  # все товары для этого поступления

    #     # Для каждого товара получаем историю цен
    #     for product in products:
    #         product.price_history = product.prod.all().order_by('-date')

    #     context = {
    #         'stockin': stockin,
    #         'products': products,
    #     }
    #     return render(request, 'your_template.html', context)