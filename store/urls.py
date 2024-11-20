from django.urls import path,include
from store.views import *

urlpatterns = [
    path('',home_page,name='home'),
    path('category/',category_page,name='category_page'),
    path('category/<int:category_id>',update_category,name='update_category')
    
]