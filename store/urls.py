from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path(
        '',
        views.index,
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
        views.OwnCompanyListView.as_view(),
        name='owncompanylist'
    ), # переменная контекста в шаблоне 'owncompany_list'
    path(
        'suppliers/',
        views.SupplierListView.as_view(),
        name='supplierlist'
    ), # переменная контекста в шаблоне 'supplier_list'
    path(
        'buyers/',
        views.BuyerListView.as_view(),
        name='buyerlist'
    ), # переменная контекста в шаблоне 'buyer_list'
    path(
        'store/<int:pk>',
        views.StockDetailView.as_view(),
        name='stockdetail'
    ), # переменная контекста в шаблоне 'stock_detail'
    path(
        'products/<int:pk>',
        views.ProductDetailView.as_view(),
        name='productdetail'
    ), # переменная контекста в шаблоне 'product'
    path(
        'owncompany/<int:pk>',
        views.OwnCompanyDetailView.as_view(),
        name='owncompanydetail'
    ), # переменная контекста в шаблоне 'owncompany'
    path(
        'supplier/<int:pk>',
        views.SupplierDetailView.as_view(),
        name='supplierdetail'
    ), # переменная контекста в шаблоне 'supplier'
    path(
        'buyer/<int:pk>',
        views.BuyerDetailView.as_view(),
        name='buyerdetail'
    ), # переменная контекста в шаблоне 'buyer'
    path(
        'stockin/',
        views.StockInListView.as_view(),
        name='stockin'
    ), # переменная контекста в шаблоне 'stockin'
    path(
        'stockout/',
        views.StockOutListView.as_view(),
        name='stockout'
    ), # переменная контекста в шаблоне 'stockout'
    # path(
    #     'stockincreate/',
    #     views.CtockInCreateView.as_view(),
    #     name='stockincreate'
    # ), # переменная контекста в шаблоне 'stockin_create'
] + debug_toolbar_urls()