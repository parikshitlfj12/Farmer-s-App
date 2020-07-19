from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sign
from django.contrib.sessions.models import Session
from vendor.models import Products, UserOrders
from .forms import Form
from project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from twilio.rest import Client
import random
# Create your views here.

def home(request) :
    if request.session.has_key('is_Logged'):
        name = request.COOKIES['username']
        password = request.COOKIES['password']
        logoutbutton = "LogOut"
        return render(request, 'index.html', {'username': name, 'password': password, 'logout': logoutbutton})
    else:
        return render(request, 'index.html')

def myorders(request): 
    if request.session.has_key('is_Logged'):
        name = request.COOKIES['username']
        password = request.COOKIES['password']
        logoutbutton = "LogOut"
        allorders = UserOrders.objects.all()
        specificorders = []
        for everyorder in allorders:
            if everyorder.name == name:
                specificorders.append(everyorder)
        return render(request, 'myorders.html', {'username': name, 'password': password, 'logout': logoutbutton, 'orderlist': specificorders})
    else:
        return render(request, 'login.html')

def shop(request) :
    if request.method == 'POST':
        if request.session.has_key('is_Logged'):
            name = request.COOKIES['username']
            password = request.COOKIES['password']
            logoutbutton = "LogOut"
            allproducts = Products.objects.all()
            name = []
            for x in allproducts:
                name.append(x.name)
            cart = request.session.get('cart')
            Product = random.choice(name) 
            if cart:
                quantity = cart.get(Product)
                if quantity:
                    cart[Product] = quantity+1
                else:
                    cart[Product] = 1
            else:
                cart = {}
                cart[Product] = 1

            request.session['cart'] = cart
            cartitems = request.session['cart']
            pri = 0
            for x,y in cartitems.items():
                for prod in allproducts:
                    if prod.name == x:
                        cartitems[x] = prod.price
                        pri += prod.price
            return render(request, 'shop.html', {'allproducts': allproducts, 'username': name, 'password': password, 'logout': logoutbutton, 'cartitems': cartitems, 'pri': pri})

        else:
            return render(request, 'login.html')
    else:
        if request.session.has_key('is_Logged'):
            name = request.COOKIES['username']
            password = request.COOKIES['password']
            logoutbutton = "LogOut"
            allproducts = Products.objects.all()
            if request.session.has_key('cart'):
                cartitems = request.session['cart']
                return render(request, 'shop.html', {'allproducts': allproducts, 'username': name, 'password': password, 'logout': logoutbutton, 'cartitems': cartitems})
            else:
                return render(request, 'shop.html', {'allproducts': allproducts, 'username': name, 'password': password, 'logout': logoutbutton})
        else:
            return render(request, 'login.html')




def contact(request) :
    sub = Form()
    if request.method == 'POST':
        # # Send Mail
        # sub = Form(request.POST)
        # subject = 'Happy Farm Welcomes You.'
        # message = 'Thank you for contacting us! Our Customer Care Support will shortly call you.'
        # recepient = str(sub['Email'].value())
        # send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

        
        # # Send SMS
        # username = request.POST['name']
        # email = request.POST['Email']
        # phone = request.POST['phone']

        # client = Client()
        # sms = client.messages.create(
        #     from_ = '+12019077950',
        #     body= 'Greetings, Welcome to happy farm. You requested us to call you back for information about our platform. Our Customer care services will shortly call you. Thank you for contacting Happy Farm. Have a good day. Thank YOu.',
        #     to='+917357989911'
        # )
        # print(sms.sid)


        return HttpResponse("Success")

        # 
        # return render(request, 'index.html', {'recepient': recepient})
    return render(request, 'contact.html', {'form':sub})
    # return render(request, 'contact.html')

def sendmail(request):
    sub = Form(request.POST)
    subject = 'Happy Farm Welcomes You.'
    message = 'Thank you for contacting us! Our Customer Care Support will shortly call you.'
    recepient = str(sub['Email'].value())
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return redirect('http://localhost:8000/')

def changepass(request) :
    return render(request, 'changepass.html')
    
def change(request):
    return render(request, 'login.html')

def about(request) :
    return render(request, 'about.html')

def addtocart(request):
    return render(request, 'shop.html')

def checkout(request):
    if request.session.has_key('cart'):
        if request.session.has_key('is_Logged'):
            name = request.COOKIES['username']
            password = request.COOKIES['password']
            logoutbutton = "LogOut"

            cartitems = request.session['cart']
            aallproducts = Products.objects.all()
            nameprice = {}
            total = 0
            for item in cartitems:
                for prod in aallproducts:
                    if item == prod.name:
                        nameprice[item] = prod.price
                        total += prod.price
            return render(request, 'checkout.html', {'cartitems': nameprice, 'total': total, 'username': name, 'password': password, 'logout': logoutbutton})
    else:
        return render(request, 'checkout.html')

def pay(request):
    mode = request.POST['mode']
    totalprice = request.POST['totalprice']
    if mode == 'COD':
        cart = request.session['cart']
        list=[]
        for x in cart: 
            list.append(x)
        order = UserOrders()
        order.name = name = request.COOKIES['username']
        order.mode = 'Cash On Delivery'
        order.list = list
        order.totalprice = totalprice
        order.save()
        del request.session['cart']
        return redirect('http://localhost:8000')
    elif mode == 'paypal':
        cart = request.session['cart']
        list=[]
        for x in cart: 
            list.append(x)
        order = UserOrders()
        order.name = name = request.COOKIES['username']
        order.mode = 'PayPal'
        order.list = list
        order.totalprice = totalprice
        order.save()
        # Make Payments
        del request.session['cart']
        response = render(request, 'test.html', {'totalamount': totalprice})
        return response

def test(request):
    total = request.COOKIES['total']
    print('Test sections========')
    print("TOTAL PRICE", total)
    return render(request, 'test.html',{'totalamount': total})