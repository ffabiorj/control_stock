from django.urls import path
from stock import views as v

app_name = 'stock'

urlpatterns = [
    path('', v.stock_entry_list, name='stock_entry_list'),
]
