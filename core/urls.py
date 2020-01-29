from django.urls import path
from core import views as view

app_name = 'core'

urlpatterns = [
    path('', view.index, name='index'),
]