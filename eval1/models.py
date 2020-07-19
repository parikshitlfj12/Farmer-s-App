from django.db import models

# Create your models here.
class Sign( models.Model):
    username = models.CharField(max_length=100)
    email = models.TextField(max_length=100)
    passwd = models.TextField(max_length=100)
    phone = models.TextField(max_length=20)
    buyorsell = models.TextField(max_length=10)


class Customer( models.Model):
    username = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    email = models.TextField(max_length=30)
    state = models.TextField(max_length=100)
    postal = models.TextField(max_length=20)
    address = models.TextField(max_length=100)
    phone = models.TextField(max_length=30)
    status = models.BooleanField(default=False) 
