# forms.py 
from django import forms 
from .models import *
  
class ProductForm(forms.ModelForm): 
  
    class Meta: 
        model = Products 
        fields = ['name','desc','price','stock','image'] 