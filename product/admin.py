from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'importado',
        'ncm',
        'preco',
        'estoque',
        'estoque_minimo',
    )
    search_fields=('produto',)
    list_filter=('importado',)
