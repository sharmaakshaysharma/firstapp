from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home_page(request):
    return render(request,'store/home.html')  


def category_page(request):
    if request.method == 'POST':
        form = CategoryType(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully')
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


def coverType_page(request):
    if request.method == 'POST':
        form=CoverTypes(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coverType_page')
    else:
        form=CoverType()

    covertypes=CoverType.objects.all()
    return render(request,'store/coverType.html',{'form':form,'covertypes':covertypes})


def update_coverType(request):
    if request.method == 'POST':
        coverType_id = request.POST.get('coverType_id')
        coverType = get_object_or_404(CoverType, id=coverType_id)
        form = CoverTypes(request.POST, instance=coverType)
        if form.is_valid():
            form.save()
    return redirect('coverType_page')

def delete_coverType(request):
    if request.method == 'POST':
        coverType_id = request.POST.get('coverType_id')
        coverType = get_object_or_404(CoverType, id=coverType_id)
        coverType.delete()
    return redirect('coverType_page')

def get_product(request):
    product=Product.objects.all()
    return render(request,'store/home.html',{'product':product})