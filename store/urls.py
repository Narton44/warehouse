from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from store import views

urlpatterns = [
    path(
        '',
        views.Index.as_view(),
        name='main'
        ),

    path(
        'stocks/',
        views.StockListView.as_view(),
        name='stocklist'
        ),

    path(
        'stocks/create',
        views.StockCreateView.as_view(),
        name='stock_create'
        ),

    path(
        'products/',
        views.ProductListView.as_view(),
        name='productlist'
    ),

    path(
        'owncompanies/',
        views.OwnCompanyListView.as_view(),
        name='owncompanylist'
    ),

    path(
        'suppliers/',
        views.SupplierListView.as_view(),
        name='supplierlist'
    ),

    path(
        'buyers/',
        views.BuyerListView.as_view(),
        name='buyerlist'
    ),

    path(
        'banks/',
        views.BankListView.as_view(),
        name='banklist'
    ),

    path(
        'store/<int:pk>',
        views.StockDetailView.as_view(),
        name='stockdetail'
    ),

    path(
        'products/<int:pk>',
        views.ProductDetailView.as_view(),
        name='productdetail'
    ),

    path(
        'owncompany/<int:pk>',
        views.OwnCompanyDetailView.as_view(),
        name='owncompanydetail'
    ),

    path(
        'supplier/<int:pk>',
        views.SupplierDetailView.as_view(),
        name='supplierdetail'
    ),

    path(
        'buyer/<int:pk>',
        views.BuyerDetailView.as_view(),
        name='buyerdetail'
    ),

    path(
        'stockin/',
        views.StockInListView.as_view(),
        name='stockin'
    ),

    path(
        'stockincreate/',
        views.StockInCreateView.as_view(),
        name='stockincreate'
    ),

    path(
        'stockin/<int:pk>',
        views.StockInDetailView.as_view(),
        name='stockincreate'
    ),

    path(
        'stockout/',
        views.StockOutListView.as_view(),
        name='stockout'
    ),

] + debug_toolbar_urls()