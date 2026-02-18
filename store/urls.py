from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from store import views

urlpatterns = [
    path( # начальная страница
        '',
        views.Index.as_view(),
        name='main'
        ),

    path( # список складов
        'stocks/',
        views.StockListView.as_view(),
        name='stocklist'
        ),

    path( # создание склада
        'stocks/create',
        views.StockCreateView.as_view(),
        name='stock_create'
        ),

    path( # список товаров

        'products/',
        views.ProductListView.as_view(),
        name='productlist'
    ),

    path(  # создание карточки товара
        'products/create',
        views.ProductCreateView.as_view(),
        name='product_create'
        ),

    path(  # список своих компаний
        'owncompanies/',
        views.OwnCompanyListView.as_view(),
        name='owncompanylist'
    ),

    path( # список поставщиков
        'suppliers/',
        views.SupplierListView.as_view(),
        name='supplierlist'
    ),

    path(  # список покупателей
        'buyers/',
        views.BuyerListView.as_view(),
        name='buyerlist'
    ),

    path(  # список банков
        'banks/',
        views.BankListView.as_view(),
        name='banklist'
    ),

    path( # детальная информация о складе
        'store/<int:pk>',
        views.StockDetailView.as_view(),
        name='stockdetail'
    ),

    path( # детальная информация о товаре
        'products/<int:pk>',
        views.ProductDetailView.as_view(),
        name='productdetail'
    ),

    path(  # детальная информация о своей фирме
        'owncompany/<int:pk>',
        views.OwnCompanyDetailView.as_view(),
        name='owncompanydetail'
    ),

    path(  # детальная информация о поставщике
        'supplier/<int:pk>',
        views.SupplierDetailView.as_view(),
        name='supplierdetail'
    ),

    path(  # детальная информация о покупателе
        'buyer/<int:pk>',
        views.BuyerDetailView.as_view(),
        name='buyerdetail'
    ),

    path(  # список покупок
        'stockin/',
        views.StockInListView.as_view(),
        name='stockin'
    ),

    path( # создание покупки
        'stockincreate/',
        views.StockInCreateView.as_view(),
        name='stockincreate'
    ),

    path( # детальная информация о покупке
        'stockin/<int:pk>',
        views.StockInDetailView.as_view(),
        name='stockindetail'
    ),

    path( # список продаж
        'stockout/',
        views.StockOutListView.as_view(),
        name='stockout'
    ),

] + debug_toolbar_urls()