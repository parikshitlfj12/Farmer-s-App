from .models import Products

from  django import forms

class ProducteditForm(forms.ModelForm):
    class Meta:
        model=Products
        fields="__all__"
