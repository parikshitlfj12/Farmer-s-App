from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  phone = models.CharField(max_length=30)
  address = models.CharField(max_length=100)

class VendorUser(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  phone = models.CharField(max_length=30)
  address = models.CharField(max_length=100)
