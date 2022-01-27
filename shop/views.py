
from django.shortcuts import render,redirect,get_object_or_404
from .models import Product, Cart, CartItem
from django.utils import timezone


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

def add(request, id):
    #Get the product to be added to the cart
    product = get_object_or_404(Product, id=id)
    #Get item if it's already in the cart_item or create a cart_item for the product
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user, ordered=False)
    #Filter according to the current logged in user and incomplete oreders
    cart_ = Cart.objects.filter(user=request.user, ordered = False)
    #If there are any incomplete orders for the current logged in user:
    if cart_.exists():
        cart = cart_[0]
        if cart.products.filter(product__id=product.id).exists():
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart.products.add(cart_item)
    else:
        #ordered_date = timezone.now()
        cart = Cart.objects.create(user=request.user)
        cart.products.add(cart_item)
    return redirect("home")

def remove(request, id):
    #Get the product to be added to the cart
    product = get_object_or_404(Product, id=id)
    cart_ = Cart.objects.filter(user=request.user, ordered = False)
    if cart_.exists():
        cart = cart_[0]
        if cart.products.filter(product__id=product.id).exists():
            cart_item = CartItem.objects.filter(product=product, user=request.user, ordered=False)[0]
            cart_item.product.remove(cart_item)
            return redirect('home')
        else:
            return redirect('home')
    else:
        return redirect('home')

    return redirect("home")