from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products
from .forms import *
  
def signOut(request):
  del request.session['vendor_is_logged']
  response = redirect('http://localhost:8000/account/vendor-login')
  response.set_cookie('vendorloggedin', False)
  return response

def dashboard(request): 
  if request.session.has_key('vendor_is_logged'):
    vendorname = request.COOKIES['vendorname']
    vendorpassword = request.COOKIES['vendorpassword']
    logoutbutton = "LogOut"
    return render(request, 'vendor/vendordashboard.html', {'username': vendorname, 'password': vendorpassword, 'logout': logoutbutton})
  else:
    return redirect('http://localhost:8000/account/vendor-login')

def orders(request): 
  return(render(request, 'vendor/orders.html'))

def products(request): 
  vendorproducts = Products.objects.all()
  return(render(request, 'vendor/products.html', {'products': vendorproducts}))

def add_new_product(request):
    if request.method == 'POST': 
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return redirect('http://localhost:8000/vendor/products/')
    else: 
        form = ProductForm() 
        return render(request, 'vendor/products.html') 


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

