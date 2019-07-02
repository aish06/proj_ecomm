import random
import os
from django.db import models
from retailer_profile.models import Retailer



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance, filename):
   # print(instance)
   # print(filename)
   new_filename = random.randint(1, 868686)
   name, ext = get_filename_ext(filename)
   final_filename = f'{new_filename}{ext}'
   return "cakes/images/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs=self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None



class Cake(models.Model):
    cake_id = models.CharField(max_length=120,unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    retailer = models.ForeignKey(Retailer,on_delete=models.CASCADE)
    size = models.DecimalField(decimal_places=1, max_digits=20, default=1.0)
    flavour = models.CharField(max_length=100)


    objects=ProductManager()

    def __str__(self):
        return self.cake_id



