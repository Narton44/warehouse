from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Stock, Product, OwnCompany, Supplier, Buyer

class StockListView(ListView):
    model = Stock
    template_name = 'store/index.html'
    context_object_name = 'stock_list'

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product_list'

class OwnCompanyList(ListView):
    model = OwnCompany
    template_name = 'store/own_company_list.html'
    context_object_name = 'owncompany_list'

class SupplierList(StockListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier_list'

class BuyerList(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer_list'

class StockProductList(ListView):
    model = Product
    template_name = 'store/stock_product_list.html'
    context_object_name = 'stock_product_list'

    def get_queryset(self): # Достаём товары только на данном складе
        stock_id = self.kwargs['stock_id'] # Получаем stock_id из URL-параметра
        stock = get_object_or_404(Stock,id=stock_id) # Находим склад по id (или по др. полю, напр., slug)
        return Product.objects.filter(stock = stock)
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail_view.html'
    context_object_name = 'product_detail'