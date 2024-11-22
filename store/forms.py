from django import forms
from .models import *



class CategoryType(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CoverTypes(forms.ModelForm):
    class Meta:
        model = CoverType
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','author','description','isbn','price','category','coverType','image']