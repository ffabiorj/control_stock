from django.contrib import admin
from .models import Stock, StockItems


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'invoice')
    search_fields = ('invoice',)
    list_filter = ('employ',)
    date_hierarchy = 'created'