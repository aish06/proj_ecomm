from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView

from .models import Cake
from django.http import Http404


def cake_list_view(request):
    queryset=Cake.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,"cake/list.html",context)


def cake_detail_view(request,pk=None,*args,**kwargs):
    # instance=Product.objects.get(pk=pk)
    #instance=get_object_or_404(Product,pk=pk)
    # try:
    #     instance=Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print("no product here")
    #     raise Http404("Product does not exist")
    # except:
    #     print("huh?")
    instance=Cake.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Cake does not exist")


    context={
        'object':instance
    }
    return render(request,"cake/detail.html",context)

