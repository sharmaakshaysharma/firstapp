from django.urls import path,include
from store.views import *

urlpatterns = [
    path('',get_product,name='home'),
    path('category/',category_page,name='category_page'),
    path('category/update/', update_category, name='update_category'),
    path('category/delete/', delete_category, name='delete_category'), 
    path('coverType/',coverType_page,name='coverType_page'),
    path('coverType/update/', update_coverType, name='update_coverType'),
    path('coverType/delete/', delete_coverType, name='delete_coverType'),
    path('product/',product_page,name='product_page'),
    path('product/<int:id>',view_product,name='view_product'),
    
]       