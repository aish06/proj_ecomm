from django.db import models
from django.contrib.auth import authenticate,login,get_user_model,logout

class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs=self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

class Retailer(models.Model):
    name=models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address=models.TextField()
    gstno=models.IntegerField()
    aadhar=models.IntegerField()

    def __str__(self):
        return self.username
