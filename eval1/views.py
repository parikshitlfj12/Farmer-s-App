from django.shortcuts import render
from django.http import HttpResponse
from .models import Sign,Products,History,Ingredients
from django.utils import timezone
import datetime
from .form import ProducteditForm
# Create your views here.

def home(request) :
    return render(request, 'index.html')

def history(request):
    histry=History.objects.all()
    return render(request,'history.html',{'data':histry})

def bill(request):
    return render(request,'bill.html')

def contact(request) :
    return render(request, 'contact.html')

def changepass(request) :
    return render(request, 'changepass.html')
    
def change(request):
    return render(request, 'login.html')


def about(request) :
    return render(request, 'about.html')

def checkout(request):
    return render(request, 'checkout.html')

def login(request) :
    return render(request, 'login.html')
    
def signup(request) :
    return render(request, 'signup.html')

def signuppost(request) :
    product=Products(
    productname="cake",
    ingredients="cream,milk,egg",
    price="100",
    weight ="22",
    order_id="1",
    date=timezone.now()
    )
    product.save()
    return render(request, 'index.html')

def Supply(request):
    if request.method =="GET":
        product=Ingredients.objects.all()
        return render(request,"Supply.html",{'data':product})
    if request.method =='POST':
        Name=request.POST['Name']
        Order_ID=request.POST['Order_ID']
        Ingredient=request.POST['Ingredients']
        Price=request.POST['Price']
        Weight = request.POST['Weight']
        product=Products(productname=Name,ingredients=Ingredient,price=Price,weight =Weight,order_id=Order_ID,date=timezone.now())
        product.save()
        prdcts=Products.objects.all()
        return render(request,'prdctlst.html',{'data':prdcts})
    
def loginpost(request) :
    return render(request, 'index.html')

def product(request):
    prdcts=Products.objects.all()
   
    return render(request,'prdctlst.html',{'data':prdcts})

def edit(request,product_id):
    if request.method =="GET":
        product=Products.objects.get(id=product_id)
        form=ProducteditForm(instance=product)
        return render(request,"Checkout.html",{'data':product})
    if request.method == "POST":
        product=Products.objects.get(id=product_id)
        ProductName=product.productname
        Order_ID=product.order_id
        Ingredients=product.ingredients
        Price=product.price
        Buyer_name="rahul"
        Weight = 50
        Name=request.POST['Name']
        Phone=request.POST['PHONE']
        Adress=request.POST['Adress']
        history=History(name=Name,phone=Phone,adress=Adress,productname=ProductName,ingredients=Ingredients,price=Price,weight =Weight,order_id=Order_ID,date=timezone.now())
        history.save()
        instance = Products.objects.get(id=product.id)
        instance.delete()
        return render(request,"bill.html",{'data':product})

def Ingredient(request):
    return render(request,"Ingredients.html")

def AddIngredients(request):
    if request.method == "POST":
        Item=request.POST['Item']
        Price=request.POST['Price']
        Supplier_name=request.POST['Name']
        ingredient=Ingredients(price=Price,item=Item,supplier_name=Supplier_name,date=timezone.now())
        ingredient.save()
        
    return render(request,"addingredients.html")

    