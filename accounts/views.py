from django.shortcuts import render, redirect
from .models import User, VendorUser, CustomerProfile
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth.models import auth
from django.template import RequestContext
# Create your views here.

def logout(request):
  del request.session['is_Logged']
  return render(request, 'index.html')

def userLogin(request): 
  if request.method=='POST':
    userlist = User.objects.all()
    flag = 0
    for user in userlist:
      print("UESRS ARE ====", user.name)
      if (user.password==request.POST['passwd'] and user.name == request.POST['username']):
        request.session.clear()
        flag = 1
        request.session['is_Logged'] = True
        response = redirect('http://localhost:8000/')
        response.set_cookie('userloggedin', True)
        response.set_cookie('username', user.name)
        response.set_cookie('password', user.password)
        return response
    if flag == 0:
      messages.info(request,"Invalid User Credentials")
      response = render(request, 'login.html')
      response.set_cookie('isLogged', False)
      return response

  else:
    return render(request, 'login.html')

def userRegister(request):
  if request.method == 'POST':
    user = User()
    user.name = request.POST['username']
    user.email = request.POST['email']
    user.password = request.POST['passwd']
    user.phone = request.POST['phone']
    user.address = request.POST['address']
    user.save()
    return redirect('/account/user-login')
  else: 
    return render(request, 'signup.html')
  
# Vendor SECTION
# Vendor Login
def vendorLogin(request): 
  if request.method=='POST':
    vendorlist = VendorUser.objects.all()
    flag = 0
    for vendor in vendorlist:
      if (vendor.password==request.POST['passwd'] and vendor.name == request.POST['username']):
        request.session['vendor_is_logged'] = True
        response = redirect('http://localhost:8000/vendor/')
        flag = 1
        response.set_cookie('vendorloggedin', True)
        response.set_cookie('vendorname', vendor.name)
        response.set_cookie('vendorpassword', vendor.password)
        return response
    if flag == 0:
      messages.info(request,"Invalid Vendor Credentials")
      return render(request, 'vendor/vendor-login.html')

  else:
    return render(request, 'vendor/vendor-login.html')

def vendorRegister(request):
  if request.method == 'POST':
    vendoruser = VendorUser()
    vendoruser.name = request.POST['username']
    vendoruser.email = request.POST['email']
    vendoruser.password = request.POST['passwd']
    vendoruser.phone = request.POST['phone']
    vendoruser.address = request.POST['address']
    vendoruser.save()
    return render(request, 'vendor/vendor-login.html')
  else: 
    return render(request, 'vendor/vendor-signup.html')

def vendorChangepass(request): 
  return render(request,'vendor/vendor-changepass.html')





# Customer Login
def customerLogin(request): 
  if request.method=='POST':
    customerlist = CustomerProfile.objects.all()
    flag = 0
    for customer in customerlist:
      if (customer.password==request.POST['passwd'] and customer.name == request.POST['username']):
        request.session['customer_is_logged'] = True
        response = redirect('http://localhost:8000/customerservice/')
        flag = 1
        response.set_cookie('customerloggedin', True)
        response.set_cookie('customername', customer.name)
        response.set_cookie('customerpassword', customer.password)
        return response
    if flag == 0:
      messages.info(request,"Invalid customer Credentials")
      return render(request, 'customer/customer-login.html')
  
  else:
    return render(request, 'customer/customer-login.html')

def customerRegister(request):
  if request.method == 'POST':
    customeruser = CustomerProfile()
    customeruser.name = request.POST['username']
    customeruser.email = request.POST['email']
    customeruser.password = request.POST['passwd']
    customeruser.phone = request.POST['phone']
    customeruser.address = request.POST['address']
    customeruser.save()
    return render(request, 'customer/customer-login.html')
  else: 
    return render(request, 'customer/customer-signup.html')

def customerChangepass(request): 
  return render(request,'customer/customer-changepass.html')