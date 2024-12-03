from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns = [
    path('place/', place_order, name='place_order'),
    path('payment/<int:order_id>/', payment, name='payment'),
    path('confirmation/<int:order_id>/', order_confirmation, name='confirmation'),
    path('showorder/', show_order, name='show_order'),
]
