from django.shortcuts import render
from product.models import Product

def product_list(request):
    template_name = 'product_list.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)