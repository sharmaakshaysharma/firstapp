from django.urls import path,include
from django.contrib.auth.views import LogoutView
from accounts.views import login_page,register_page
urlpatterns=[
    path('login/',login_page,name='login_page'),
    path('register/',register_page,name='register'),
    path('logout/', LogoutView.as_view(next_page='login_page'), name='logout'),
]