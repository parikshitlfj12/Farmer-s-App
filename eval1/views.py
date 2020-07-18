from django.shortcuts import render
from django.http import HttpResponse
from .models import Sign
from vendor.models import Products

# Create your views here.

def home(request) :
    return render(request, 'index.html')

def shop(request) :
    allproducts = Products.objects.all()
    return render(request, 'shop.html', {'allproducts': allproducts})

def contact(request) :
    return render(request, 'contact.html')

def changepass(request) :
    return render(request, 'changepass.html')
    
def change(request):
    return render(request, 'login.html')


def about(request) :
    return render(request, 'about.html')

def addtocart(request):
    return render(request, 'shop.html')

def checkout(request):
    return render(request, 'checkout.html')
