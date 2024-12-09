import requests
from django.conf import settings

def search_books(query, max_results=40):
    """
    Search for books using the Google Books API.
    """
    api_key = settings.GOOGLE_BOOKS_API_KEY
    url = f"https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "maxResults": max_results,
        "key": api_key,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data from Google Books API"}