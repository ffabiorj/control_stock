from django.urls import path
from stock import views as view

app_name = 'stock'

urlpatterns = [
    path('', view.stock_entry_list, name='stock_entry_list'),
    path('detalhe-estoque/<int:pk>/', view.stock_entry_detail, name='stock_entry_detail'), 
    path('add/', view.stock_entry_add, name='stock_entry_add'),
]
