from django.shortcuts import render, redirect
from .models import User, VendorUser
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
  
def vendorLogin(request): 
  if request.method=='POST':
    pass
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