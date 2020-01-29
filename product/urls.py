from django.urls import path
from product import views as view

app_name='product'

urlpatterns=[
    path('', view.product_list, name='product_list')
]