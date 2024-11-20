from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return render(request,'store/home.html')  


def category_page(request):
    if request.method == 'POST':
        form = CategoryType(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_page')
    else:
        form = CategoryType()

    categories = Category.objects.all()     
    return render(request, 'store/category.html', {'form': form, 'categories': categories})


def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = CategoryType(request.POST, instance=category)  
        if form.is_valid():
            form.save()  # This will update the existing category
            return redirect('category_page')  # Redirect to the category list or another page
    else:
        form = CategoryType(instance=category)  # Pre-populate form with existing data

    return render(request, 'store/category.html', {'form': form, 'category': category})