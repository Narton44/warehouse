from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.StockListView.as_view(),
        name='stocklist'
        ), # переменная контекста в шаблоне 'stock_list'
]