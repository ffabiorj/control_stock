from django.shortcuts import render
from .models import Stock

def stock_entry_list(request):
    template_name = 'stock_entry_list.html'
    stocks = Stock.objects.filter(movimento='e')
    context = {
        'stocks': stocks
    }
    return render(request, template_name, context)
