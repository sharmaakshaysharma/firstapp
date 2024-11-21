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


def update_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        form = CategoryType(request.POST, instance=category)
        if form.is_valid():
            form.save()
    return redirect('category_page')

def delete_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        category.delete()
    return redirect('category_page')