from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request) :
    return render(request, 'index.html')

def shop(request) :
    return render(request, 'shop.html')

def form(request) :
    return render(request, 'form.html')

def formpost(request) :
    user = request