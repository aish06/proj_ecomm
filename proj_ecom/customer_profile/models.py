from django.db import models
from django.contrib.auth import authenticate,login,get_user_model,logout

User=get_user_model()



class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs=self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

class Customer(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()

    def __str__(self):
        return self.username


