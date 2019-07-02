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
    # print(args)
    # print(kwargs)
    #instance = Cake.objects.get(pk=pk)
    instance=get_object_or_404(Cake,pk=pk)
    if instance is None:
        raise Http404("Product does not exist")
    context = {
        'object':instance
    }
    return render(request, "cake/detail.html", context)
