from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('place/', views.place_order, name='place_order'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path('confirmation/<int:order_id>/', views.order_confirmation, name='confirmation'),
]
