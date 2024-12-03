import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem,Address
from cart.models import Cart  
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def place_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        items = data.get('items', [])
        if not items:
            return JsonResponse({'error': 'No items selected'}, status=400)
        order = Order.objects.create(user=request.user, total=0)
        total = 0
        for item in items:
            cart_item = Cart.objects.get(id=item['cart_id'], user=request.user)
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=item['quantity'],
                price=cart_item.product.price,
            )
            total += cart_item.product.price * item['quantity']
        order.total = total
        order.save()
        cart_item.delete()
        return JsonResponse({'success': True, 'order_id': order.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def payment(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)   
    context={
        'order':order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    if request.method == "POST":
        try:  
            address = Address.objects.create(
                user=request.user,
                order=order,
                name = request.POST.get('name'),    
                line1=request.POST.get('address_line1'),
                line2=request.POST.get('address_line2'),
                city=request.POST.get('city'),
                state=request.POST.get('state'),
                zip_code=request.POST.get('zip'),
                country=request.POST.get('country')
            )      
            charge = stripe.Charge.create(
                amount=int(order.total * 100),  
                currency='usd',
                source=request.POST['stripeToken'],   
                description=f"Order {order.id}",
            )
            order.is_paid = True
            order.save()

            return redirect('orders:confirmation', order_id=order.id)
        except stripe.error.StripeError as e:
            return render(request, 'orders/payment.html', {'order': order, 'error': str(e)})
    return render(request, 'orders/payment.html',context)


@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/confirmation.html', {'order': order})
