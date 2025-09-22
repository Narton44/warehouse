from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path(
        '',
        views.StockListView.as_view(),
        name='main'
        ), # переменная контекста в шаблоне 'main'
    path(
        'stocks/',
        views.StockListView.as_view(),
        name='stocklist'
        ), # переменная контекста в шаблоне 'stock_list'
    path(
        'products/',
        views.ProductListView.as_view(),
        name='productlist'
    ), # переменная контекста в шаблоне 'product_list'
    path(
        'owncompanies/',
        views.OwnCompanyList.as_view(),
        name='owncompanylist'
    ), # переменная контекста в шаблоне 'owncompany_list'
    path(
        'suppliers/',
        views.SupplierList.as_view(),
        name='supplierlist'
    ), # переменная контекста в шаблоне 'supplier_list'
    path(
        'buyers/',
        views.BuyerList.as_view(),
        name='buyerlist'
    ), # переменная контекста в шаблоне 'buyer_list'
    path(
        'store/<int:stock_id>/products',
        views.StockProductList.as_view(),
        name='stockproductlist'
    ), # переменная контекста в шаблоне 'stock_product_list'
    path(
        'store/products/<int:pk>',
        views.ProductDetailView.as_view(),
        name='productdetail'
    ), # переменная контекста в шаблоне 'product_detail'
] + debug_toolbar_urls()