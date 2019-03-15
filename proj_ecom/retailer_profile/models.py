from django.db import models
from django.contrib.auth import authenticate,login,get_user_model,logout



class Retailer(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    address=models.TextField()
    gstn=models.IntegerField()
    aadhar=models.IntegerField()
