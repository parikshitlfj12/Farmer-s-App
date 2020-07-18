from django.shortcuts import render
from django.http import HttpResponse
from .models import Sign
from django.contrib.sessions.models import Session
from vendor.models import Products

# Create your views here.

def home(request) :
    if request.session.has_key('is_Logged'):
        name = request.COOKIES['username']
        password = request.COOKIES['password']
        logoutbutton = "LogOut"
        return render(request, 'index.html', {'username': name, 'password': password, 'logout': logoutbutton})
    else:
        return render(request, 'index.html')

def shop(request) :
    if request.session.has_key('is_Logged'):
        name = request.COOKIES['username']
        password = request.COOKIES['password']
        logoutbutton = "LogOut"
        allproducts = Products.objects.all()
        return render(request, 'shop.html', {'allproducts': allproducts, 'username': name, 'password': password, 'logout': logoutbutton})
    else:
        return render(request, 'login.html')

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
