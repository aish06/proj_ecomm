from django.db import models
from django.contrib.auth import authenticate,login,get_user_model,logout

User=get_user_model()

class Customer(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact=models.IntegerField()

