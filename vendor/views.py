from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products, UserOrders
from accounts.models import VendorUser
from .forms import *
  
def signOut(request):
  del request.session['vendor_is_logged']
  response = redirect('http://localhost:8000/account/vendor-login')
  response.set_cookie('vendorloggedin', False)
  return response

def dashboard(request): 
  if request.session.has_key('vendor_is_logged'):
    order = UserOrders.objects.all()
    ordlen = len(order)
    order = order[0:4]
    vendorname = request.COOKIES['vendorname']
    vendorpassword = request.COOKIES['vendorpassword']
    logoutbutton = "LogOut"
    return render(request, 'vendor/vendordashboard.html', {'ordlen': ordlen,'orderlist': order,'vendorname': vendorname, 'password': vendorpassword, 'logout': logoutbutton})
  else:
    return redirect('http://localhost:8000/account/vendor-login')

def orders(request): 
  order = UserOrders.objects.all()
  vendorname = request.COOKIES['vendorname']
  return(render(request, 'vendor/orders.html', {'orderlist': order, "vendorname": vendorname}))

def products(request): 
  vendorproducts = Products.objects.all()
  vendorname = request.COOKIES['vendorname']
  return(render(request, 'vendor/products.html', {'products': vendorproducts, "vendorname": vendorname}))

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
  vendorname = request.COOKIES['vendorname']
  if request.method == "POST":
    return(render(request, 'vendor/coupons.html',{'vendorname': vendorname}))
  else: 
    return(render(request, 'vendor/coupons.html',{'vendorname': vendorname}))

def aboutme(request): 
  if request.session.has_key('vendor_is_logged'):
    vendorname = request.COOKIES['vendorname']
    profile = VendorUser.objects.filter(name=vendorname)

    return(render(request, 'vendor/aboutme.html',{'profile': profile[0], 'vendorname': vendorname}))
  else:
    return redirect('http://localhost:8000/')

