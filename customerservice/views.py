from django.shortcuts import render, redirect
from django.http import HttpResponse
from vendor.models import Products, UserOrders
from accounts.models import VendorUser, CustomerProfile
from eval1.models import Customer
from vendor.forms import *
  
def signOut(request):
  del request.session['customer_is_logged']
  response = redirect('http://localhost:8000/account/customer-login')
  response.set_cookie('customerloggedin', False)
  return response

def dashboard(request): 
  if request.session.has_key('customer_is_logged'):
    customerlist = Customer.objects.all()
    custlen = len(customerlist)
    customerlist = customerlist[:1]
    customername = request.COOKIES['customername']
    customerpassword = request.COOKIES['customerpassword']
    logoutbutton = "LogOut"
    return render(request, 'customer/customerdashboard.html', {'ordlen': custlen,'orderlist': customerlist,'vendorname': customername, 'password': customerpassword, 'logout': logoutbutton})
  else:
    return redirect('http://localhost:8000/account/customer-login')

def aboutme(request): 
  if request.session.has_key('customer_is_logged'):
    customername = request.COOKIES['customername']
    profile = CustomerProfile.objects.filter(name=customername)

    return(render(request, 'customer/aboutme.html',{'profile': profile[0], 'vendorname': customername}))
  else:
    return redirect('http://localhost:8000/')

def customerlist(request):
  if request.method=="POST":
    if request.session.has_key('customer_is_logged'):
      print("THE VALUE IS --------", request.POST['username'])
      
      # Render
      customername = request.COOKIES['customername']
      profile = CustomerProfile.objects.filter(name=customername)
      customerlist = Customer.objects.all()
      return(render(request, 'customer/customerlist.html',{'profile': profile[0], 'vendorname': customername, 'customerlist': customerlist}))
    else:
      return redirect('http://localhost:8000/')
  else:
    if request.session.has_key('customer_is_logged'):
      customername = request.COOKIES['customername']
      profile = CustomerProfile.objects.filter(name=customername)
      customerlist = Customer.objects.all()
      return(render(request, 'customer/customerlist.html',{'profile': profile[0], 'vendorname': customername, 'customerlist': customerlist}))
    else:
      return redirect('http://localhost:8000/')