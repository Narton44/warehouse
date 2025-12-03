from django.shortcuts import render
from django.db.models import Sum, F
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Stock, Product, OwnCompany, Supplier, Buyer, StockIn, StockOut, Bank
# from .forms import CtockInCreationForm

def index(request):
    prod_num = Product.objects.all().count()
    # stats = Product.objects.aggregate(
    #     prod_quan = Sum('quantity'),
    #     prod_total_cost = Sum(F('quantity') * F('price'))
    # )

    # prod_quan = stats['prod_quan'] or 0
    # prod_total_cost = stats['prod_total_cost'] or 0

    return render(
        request,
        'index.html',
        context=
            {
                'prod_num':prod_num,
            },
        )

class StockListView(ListView):
    model = Stock
    template_name = 'store/stock_list.html'
    context_object_name = 'stock_list'

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product_list'

class OwnCompanyListView(ListView):
    model = OwnCompany
    template_name = 'store/own_company_list.html'
    context_object_name = 'owncompany_list'

class BankListView(ListView):
    model = Bank
    template_name = 'store/bank_list.html'
    context_object_name = 'bank_list'

class SupplierListView(StockListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier_list'

class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer_list'

class StockDetailView(DetailView):
    model = Stock
    template_name = 'store/stock_detail.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_product_list'] = Product.objects.filter(stock=self.object)
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail_view.html'
    context_object_name = 'product'

class OwnCompanyDetailView(DetailView):
    model = OwnCompany
    template_name = 'store/owncompany_detail_view.html'
    context_object_name = 'owncompany'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'store/supplier_detail_view.html'
    context_object_name = 'supplier'

class BuyerDetailView(DetailView):
    model = Buyer
    template_name = 'store/buyer_detail_view.html'
    context_object_name = 'buyer'

class StockInListView(ListView):
    model = StockIn
    template_name = 'store/stockin_list.html'
    context_object_name = 'stockin'

class CtockInCreateView(ListView):
    pass

class CtockInDetailView(DetailView):
    pass

class StockOutListView(ListView):
    model = StockOut
    template_name = 'store/stockout_list.html'
    context_object_name = 'stockout'