from django.urls import path
from .views import search_books_view

urlpatterns = [
    path("search/", search_books_view, name="search_books"),
]
