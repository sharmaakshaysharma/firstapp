from django.shortcuts import render
from .utils import search_books
from django.contrib.auth.decorators import login_required


def search_books_view(request):
    query = request.GET.get("q", "")
    if query:
        data = search_books(query)
        books = data.get("items", [])
    else:
        default_query = "bestsellers"  
        data = search_books(default_query)
        books = data.get("items", [])

    return render(request, "googlebook/search.html", {"query": query, "books": books})
