from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sign
from django.contrib.sessions.models import Session
from vendor.models import Products, UserOrders

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

            cart = request.session.get('cart')
            Product = request.POST['product']
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
            print("cart items ==> ", cartitems)
            return render(request, 'shop.html', {'allproducts': allproducts, 'username': name, 'password': password, 'logout': logoutbutton, 'cartitems': cartitems})

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
                print("cart items ==> ", cartitems)
                return render(request, 'shop.html', {'allproducts': allproducts, 'username': name, 'password': password, 'logout': logoutbutton, 'cartitems': cartitems})
            else:
                return render(request, 'shop.html', {'allproducts': allproducts, 'username': name, 'password': password, 'logout': logoutbutton})
        else:
            return render(request, 'login.html')




def contact(request) :
    return render(request, 'contact.html')

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
        response = render(request, 'test.html')
        totstr = str(totalprice)
        response.set_cookie('total', totstr)
        return response

def test(request):
    total = request.COOKIES['total']
    return render(request, 'test.html',{'totalamount', totalstr})