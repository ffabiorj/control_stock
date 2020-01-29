from django.shortcuts import render
from product.models import Product

def product_list(request):
    template_name = 'product_list.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name, context)


def product_detail(request, pk):
    template_name = 'product_detail.html'
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, template_name, context)