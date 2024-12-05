from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from store.models import Product,ProductView
from cart.models import Cart
from django.contrib.auth.decorators import login_required
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
    most_viewed=ProductView.objects.order_by('-view_count')[:3]
    print(f"Most viewed products: {most_viewed}")
    for item in cart_items:
        item.total_price = item.quantity * item.product.price
    if request.user.is_authenticated:
        cart_item_count = Cart.objects.filter(user=request.user).count()
    grand_total = sum(item.total_price for item in cart_items)
   
    return render(request, 'cart/cart.html', {'cart_items': cart_items,'cart_item_count': cart_item_count,'grand_total':grand_total,'most_viewed': most_viewed})


def update_cart(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        quantity = request.POST.get('quantity')
        if not quantity.isdigit() or int(quantity) < 1:
            return JsonResponse({'error': 'Invalid quantity'}, status=400)
        quantity = int(quantity)
        try:
            cart_item = Cart.objects.get(id=cart_id, user=request.user)
            cart_item.quantity = quantity
            cart_item.save()

            total_price = cart_item.quantity * cart_item.product.price
            grand_total = sum(
                item.quantity * item.product.price
                for item in Cart.objects.filter(user=request.user)
            )
            return JsonResponse({
                'message': 'Cart updated successfully',
                'total_price': total_price,
                'grand_total': grand_total
            })
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_cart_item(request, cart_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, id=cart_id)
        cart_item.delete()
        return JsonResponse({'success': True, 'message': 'Cart item deleted successfully.'})
    
    return render(request, 'cart/cart.html')


