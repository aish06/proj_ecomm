from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView

from .models import Chocolate
from django.http import Http404


def chocolate_list_view(request):
    queryset=Chocolate.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,"chocolate/list.html",context)


def chocolate_detail_view(request,pk=None,*args,**kwargs):
    # print(args)
    # print(kwargs)
    #instance = Cake.objects.get(pk=pk)
    instance=get_object_or_404(Chocolate,pk=pk)
    if instance is None:
        raise Http404("Product does not exist")
    context = {
        'object':instance
    }
    return render(request, "chocolate/detail.html", context)

