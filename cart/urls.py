from django.urls import path
from cart.views import *

urlpatterns =[
    path('addtocart/<int:product_id>/',cart_page,name='cart_page'),
    path('showcart/',show_cart,name='show_cart'),
    path('update-cart/', update_cart, name='update_cart'),
]

