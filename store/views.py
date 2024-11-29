from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from cart.models import Cart

# Create your views here.

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
    if request.user.is_authenticated:
        cart_item_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_item_count = 0
    products = Product.objects.all()
    return render(request, 'store/home.html', {'cart_item_count': cart_item_count, 'product': products})

def product_page(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('product_page')
        else:
            print("Form errors:", form.errors)  
    else:
        form = ProductForm()

    products = Product.objects.all()
    return render(request, 'store/product.html', {'form': form, 'products': products})


def update_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('product_page')
    
def delete_product(request):
    if request.method=='POST':
        product_id=request.POST.get('product_id')
        product=get_object_or_404(Product,id=product_id)
        product.delete()
    return redirect('product_page')



