from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView

from .models import Card
from django.http import Http404


def card_list_view(request):
    queryset=Card.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,"card/list.html",context)


def card_detail_view(request,pk=None,*args,**kwargs):
    # print(args)
    # print(kwargs)
    #instance = Cake.objects.get(pk=pk)
    instance=get_object_or_404(Card,pk=pk)
    if instance is None:
        raise Http404("Product does not exist")
    context = {
        'object':instance
    }
    return render(request, "card/detail.html", context)

