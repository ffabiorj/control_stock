from django.contrib import admin
from .models import Stock, StockItems


class StockItemsInLine(admin.TabularInline):
    model = StockItems
    extra = 0

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = (StockItemsInLine,)
    list_display = ('__str__', 'invoice')
    search_fields = ('invoice',)
    list_filter = ('employ',)
    date_hierarchy = 'created'