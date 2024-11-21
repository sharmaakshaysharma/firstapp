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