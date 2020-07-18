from django.shortcuts import render, redirect
from .models import User, VendorUser
from django.contrib import messages
from django.contrib.auth.models import auth
# Create your views here.


def userLogin(request): 
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
    return redirect('/login')
  else: 
    return render(request, 'signup.html')
  
# Vendor SECTION
# Vendor Login
def vendorLogin(request): 
  if request.method=='POST':
    vendorlist = VendorUser.objects.all()
    name = ''
    for vendor in vendorlist:
      if (vendor.password==request.POST['passwd'] and vendor.name == request.POST['username']):
        return render(request, 'vendor/vendordashboard.html', {'vendor': vendor})
      else:
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