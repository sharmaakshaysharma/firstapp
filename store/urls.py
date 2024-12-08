from django.urls import path,include
from store.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',get_product,name='home'),
    path('category/',category_page,name='category_page'),
    path('category/update/', update_category, name='update_category'),
    path('category/delete/', delete_category, name='delete_category'), 
    path('coverType/',coverType_page,name='coverType_page'),
    path('coverType/update/', update_coverType, name='update_coverType'),
    path('coverType/delete/', delete_coverType, name='delete_coverType'),
    path('product/',product_page,name='product_page'),  
    path('product/update',update_product,name='update_product'),
    path('product/delete',delete_product,name='delete_product'),
    path('productview/<int:product_id>/', product_view, name='product_view'),
    path('ai-response/', get_dynamic_ai_response, name='dynamic_ai_response'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)