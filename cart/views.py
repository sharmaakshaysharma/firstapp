from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from store.models import Product
from cart.models import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Cart, Product

def cart_page(request, product_id):
    if not request.user.is_authenticated:
        
        return JsonResponse({
            'message': 'You must be logged in to add items to the cart.',
            'login_url': '/login/', 
        }, status=401)  

    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({
        'message': 'Product added to cart.',
        'cart_url': 'show_cart',  
    })

def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        item.total_price = item.quantity * item.product.price
    return render(request, 'cart/cart.html', {'cart_items': cart_items})


