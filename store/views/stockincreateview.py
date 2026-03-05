from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404
from store.models import StockIn, StockInProductItem
from django.db import transaction
from store.forms import StockInCreationForm, StockInProductItemFormSet
from django.urls import reverse_lazy


class StockInCreateView(CreateView): # класс создания закупки товаров
    model = StockIn
    form_class = StockInCreationForm
    template_name = 'store/stockinadd.html'
    success_url = reverse_lazy('stockin')



    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = StockInProductItemFormSet(self.request.POST)
        else:
            data['items'] = StockInProductItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items_formset = context['items']
        with transaction.atomic():
            self.object = form.save()
            if items_formset.is_valid():
                items_formset.instance = self.object
                items_formset.save()
        return super().form_valid(form)

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