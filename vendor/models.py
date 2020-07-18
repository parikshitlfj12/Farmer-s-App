from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Products(models.Model):
  name = models.CharField(max_length=100)
  desc = models.CharField(max_length=200)
  price = models.IntegerField()
  stock = models.IntegerField()
  image = models.ImageField(upload_to='pics')

class UserOrders(models.Model):
  name = models.CharField(max_length=100)
  mode = models.CharField(max_length=100)
  list = ArrayField(ArrayField(models.CharField(max_length=20, blank=True),size=8,),size=8,)
  totalprice = models.IntegerField()