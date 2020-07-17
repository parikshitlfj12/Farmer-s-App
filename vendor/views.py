from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request) :
  return render(request, 'index.html')
def vendor_signup(request): 
  return(render(request, 'vendor/vendor-signup.html'))
def vendor_login(request): 
  return(render(request, 'vendor/vendor-login.html'))


def dashboard(request): 
  return(render(request, 'vendor/vendordashboard.html'))

def orders(request): 
  return(render(request, 'vendor/orders.html'))

def products(request): 
  return(render(request, 'vendor/products.html'));
def add_new_product(request):
  return(render(request, 'vendor/products.html'));

def coupons(request): 
  return(render(request, 'vendor/coupons.html'))
def add_new_coupon(request):
  return(render(request, 'vendor/coupons.html'))

def aboutme(request): 
  return(render(request, 'vendor/aboutme.html'))

def chart(request): 
  return(render(request, 'vendor/pages/charts/chartjs.html'))

def table(request): 
  return(render(request, 'vendor/pages/tables/basic-table.html'))

