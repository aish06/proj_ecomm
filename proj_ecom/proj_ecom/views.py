from django.http import HttpResponse
from django.contrib.auth import authenticate,login,get_user_model
from django.shortcuts import render,redirect

from customer_profile.models import Customer
from retailer_profile.models import Retailer


User=get_user_model()

def index(request):
    return render(request,"get_started.html",{})


def sign_cust_page(request):
    context={
        "uname1":False,
        "email1":False,
        "pass1":False,
        "email2":False
    }
    if request.POST:
        name=request.POST.get("name")
        email=request.POST.get("email")
        username=request.POST.get("uname")
        password=request.POST.get("psw")
        confirm_pass=request.POST.get("cnfpsw")
        phone=request.POST.get("phone")
        qs=User.objects.filter(username=username)
        qs1=User.objects.filter(email=email)
        if qs.exists():
            #username already exists
            context={
                "uname1":True
            }
        elif qs1.exists():
            #email already exists
            context = {
                "email1": True
            }
        elif password!=confirm_pass:
            #password not same
            context = {
                "pass1": True
            }
        elif not ".com" in email:
            context = {
                "email2": True
            }
        else:
            new_user=User.objects.create_user(username=username,email=email,password=password)
            cust_profile=Customer(
                name=name,
                email=email,
                username=username,
                phone=phone
            )
            cust_profile.save()
            if new_user is not None:
                return redirect("/login")
    return render(request,"auth/customer_signup.html",context)


def sign_ret_page(request):
    context = {
        "uname1": False,
        "email1": False,
        "pass1": False,
        "gstno1":False,
        "aadhar1":False,
        "email2": False
    }
    if request.POST:
        name = request.POST.get("retailer_name")
        email = request.POST.get("retailer_email")
        username = request.POST.get("retailer_uname")
        confirm_pass=request.POST.get("cnfpsw")
        password = request.POST.get("retailer_psw")
        phone = request.POST.get("retailer_phone")
        address=request.POST.get("retailer_address")
        gstno=request.POST.get("retailer_gstno")
        aadhar=request.POST.get("retailer_aadhar")
        qs = User.objects.filter(username=username)
        qs1 = User.objects.filter(email=email)
        qs2=Retailer.objects.filter(gstno=gstno)
        qs3=Retailer.objects.filter(aadhar=aadhar)
        if qs.exists():
            # username already exists
            context = {
                "uname1": True
            }
        elif qs1.exists():
            # email already exists
            context = {
                "email1": True
            }
        elif qs2.exists():
            # gstno already exists
            context = {
                "gstno1": True
            }
        elif qs3.exists():
            # aadhar already exists
            context = {
                "aadhar1": True
            }
        elif password != confirm_pass:
            # password not same
            context = {
                "pass1": True
            }
        elif not ".com" in email:
            context = {
                "email2": True
            }
        else:
            new_user=User.objects.create_user(username=username,email=email,password=password)
            retail_profile = Retailer(
                name=name,
                email=email,
                username=username,
                phone=phone,
                address=address,
                gstno=gstno,
                aadhar=aadhar,
            )
            retail_profile.save()
            if new_user is not None:
                return redirect("/login")
    return render(request, "auth/retailer_signup.html", context)

def login_page(request):
    context={
        "bool":False
    }
    if request.POST:
        username=request.POST.get("uname")
        password=request.POST.get("psw")
        category=request.POST.get("category")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if category=="cust":
                return redirect('/')
            else:
                return redirect('/')
        else:
            #wrong credentials
            context = {
                "bool": True
            }
    return render(request,"auth/login.html",context)







