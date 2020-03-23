from django.shortcuts import render
from django.http import HttpResponse
from .models import Sign

# Create your views here.

def home(request) :
    return render(request, 'index.html')

def shop(request) :
    return render(request, 'shop.html')

def login(request) :
    return render(request, 'login.html')
    
def signup(request) :
    return render(request, 'signup.html')

def signuppost(request) :
    sign = Sign(
        username='singhdon85',
        email='singhdon85@gmail.com',
        passwd='1234',
        phone='9856985698',
        buyorsell='Buy'
    )
    sign.save()
    return render(request, 'index.html')

def loginpost(request) :
    return render(request, 'index.html')

