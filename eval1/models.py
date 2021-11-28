from django.db import models

# Create your models here.
class Sign( models.Model):
    username = models.CharField(max_length=100)
    email = models.TextField(max_length=100)
    passwd = models.TextField(max_length=100)
    phone = models.TextField(max_length=20)
    buyorsell = models.TextField(max_length=10)
class Products (models.Model):
    productname=models.CharField(max_length=100)
    ingredients=models.TextField(max_length=100)
    price=models.IntegerField()
    weight =models.FloatField()
    order_id=models.IntegerField()
    date=models.DateField()
    class Meta:
        db_table="eval1_products"
    
class History(models.Model):
    Buyer_name=models.TextField(max_length=100)
    productname=models.CharField(max_length=100)
    ingredients=models.TextField(max_length=100)
    price=models.IntegerField()
    weight =models.FloatField()
    order_id=models.IntegerField()
    date=models.DateField()
    name=models.CharField(max_length=100)
    phone=models.TextField(max_length=100)
    adress=models.CharField(max_length=100)

class Ingredients(models.Model):
    item=models.TextField(max_length=100,unique=True)
    price=models.IntegerField()
    supplier_name=models.TextField(max_length=100)
    date=models.DateField()

