from django.shortcuts import render
from .models import Product


def index(request):
    return render(request,'product/index.html')

def product_list(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'product/product_list.html', context)