
from django.shortcuts import render,redirect,get_object_or_404
from .models import Product, Cart

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

def add(request,id):
        if request.user.is_authenticated():
            product = get_object_or_404(Product, id)
        else :
            cart = get_object_or_404(Cart, user=request.user)
            cart = Cart.objects.create(user = request.user)
            cart.save()
            cart.add_to_cart(id)
            return redirect('cart')
        