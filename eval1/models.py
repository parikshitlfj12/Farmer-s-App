from django.db import models

# Create your models here.
class Sign( models.Model):
    username = models.CharField(max_length=100)
    email = models.TextField(max_length=100)
    passwd = models.TextField(max_length=100)
    phone = models.TextField(max_length=20)
    buyorsell = models.TextField(max_length=10)
