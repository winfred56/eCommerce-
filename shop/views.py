from email.mime import image
from django.shortcuts import render
from .models import Product, Image

def home(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'shop/home.html', context)

def detail(request, id):
    product = Product.objects.get(id=id)

    context = {
        'product':product,
        
    }

    return render(request, 'shop/detail.html', context)