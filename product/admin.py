from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'importad',
        'ncm',
        'price',
        'stock',
        'minimum_stock',
    )
    search_fields=('product',)
    list_filter=('importad',)
