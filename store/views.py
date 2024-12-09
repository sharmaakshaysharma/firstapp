from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from cart.models import Cart
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GENAI_API_KEY)

@login_required
def category_page(request):
    if request.method == 'POST':
        form = CategoryType(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully')
            return redirect('category_page')
    else:
        form = CategoryType()
    if request.user.is_authenticated:
        cart_item_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_item_count = 0
    categories = Category.objects.all()     
    return render(request, 'store/category.html', {'form': form, 'categories': categories,'cart_item_count': cart_item_count})

@login_required
def update_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        form = CategoryType(request.POST, instance=category)
        if form.is_valid():
            form.save()
    return redirect('category_page')

@login_required
def delete_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        category.delete()
    return redirect('category_page')
@login_required
def coverType_page(request):
    if request.method == 'POST':
        form=CoverTypes(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coverType_page')
    else:
        form=CoverType()
    if request.user.is_authenticated:
        cart_item_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_item_count = 0
    covertypes=CoverType.objects.all()
    return render(request,'store/coverType.html',{'form':form,'covertypes':covertypes,'cart_item_count': cart_item_count})

@login_required
def update_coverType(request):
    if request.method == 'POST':
        coverType_id = request.POST.get('coverType_id')
        coverType = get_object_or_404(CoverType, id=coverType_id)
        form = CoverTypes(request.POST, instance=coverType)
        if form.is_valid():
            form.save()
    return redirect('coverType_page')

@login_required
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

@login_required
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
    if request.user.is_authenticated:
        cart_item_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_item_count = 0
    products = Product.objects.all()
    return render(request, 'store/product.html', {'form': form, 'products': products,'cart_item_count': cart_item_count})

@login_required
def update_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('product_page')
    
@login_required   
def delete_product(request):
    if request.method=='POST':
        product_id=request.POST.get('product_id')
        product=get_object_or_404(Product,id=product_id)
        product.delete()
    return redirect('product_page')


def product_view(request, product_id):
    product =Product.objects.get(id=product_id)
    product_view, created = ProductView.objects.get_or_create(product=product)

    product_view.view_count += 1
    product_view.save()
    
    return JsonResponse({"message": "Product view count updated", "view_count": product_view.view_count})



def get_ai_response(request):
    try:
        query = request.GET.get("query", None) 
        model_name = request.GET.get("model", "gemini-1.5-flash")
        if not query:
            return JsonResponse({"error": "The 'query' parameter is required."}, status=400)
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            query,
        )
        return JsonResponse({
            "query": query,
            "model": model_name,
            "response": response.text
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)