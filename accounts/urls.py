from django.urls import path,include
from django.contrib.auth.views import LogoutView
from accounts.views import login_page,register_page,custom_logout_view
urlpatterns=[
    path('login/',login_page,name='login_page'),
    path('register/',register_page,name='register'),
     path('logout/', custom_logout_view, name='logout')
]