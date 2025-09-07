from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path(
        '',
        views.StockListView.as_view(),
        name='stocklist'
        ), # переменная контекста в шаблоне 'stock_list'
] + debug_toolbar_urls()