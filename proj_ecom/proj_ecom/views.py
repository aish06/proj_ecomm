from django.http import HttpResponse
from django.contrib.auth import authenticate,login,get_user_model
from django.shortcuts import render,redirect

from customer_profile.models import Customer
from retailer_profile.models import Retailer

from cake.models import Cake

from bouquet.models import Bouquet
from cards.models import Card
from chocolates.models import Chocolate
from Watches.models import Watch





User=get_user_model()

def signup_page(request):
    context = {
        "uname1": False,
        "email1": False,
        "pass1": False,
        "email2": False,
        "gstno1": False,
        "aadhar1": False,
        "category":False,
    }
    if request.POST:
        category=request.POST.get("category")
        if category=="cust":
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            username = request.POST.get("uname")
            password = request.POST.get("psw")
            confirm_pass = request.POST.get("cnfpsw")
            phone = request.POST.get("phone")
            qs = User.objects.filter(username=username)
            qs1 = User.objects.filter(email=email)
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
                new_user = User.objects.create_user(username=username, email=email, password=password)
                cust_profile = Customer(
                    name=firstname+" "+lastname,
                    email=email,
                    username=username,
                    phone=phone,
                )
                cust_profile.save()
                if new_user is not None:
                    return redirect("/login")
        elif category=="ret":
            firstname = request.POST.get("retailer_firstname")
            lastname = request.POST.get("retailer_lastname")
            email = request.POST.get("retailer_email")
            username = request.POST.get("retailer_uname")
            confirm_pass = request.POST.get("retailer_cnfpsw")
            password = request.POST.get("retailer_psw")
            phone = request.POST.get("retailer_phone")
            address = request.POST.get("retailer_address")
            gstno = request.POST.get("retailer_gstno")
            aadhar = request.POST.get("retailer_aadhar")
            qs = User.objects.filter(username=username)
            qs1 = User.objects.filter(email=email)
            qs2 = Retailer.objects.filter(gstno=gstno)
            qs3 = Retailer.objects.filter(aadhar=aadhar)
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
                new_user = User.objects.create_user(username=username, email=email, password=password)
                retail_profile = Retailer(
                    name=firstname + " " + lastname,
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
        else:
            # category not selected
            context = {
                "category": True
            }
    return render(request,"auth/signup.html",context)



def homepage(request):
    return render(request,"get_started.html",{})


def index(request):
    cake_query=Cake.objects.all()[:5]
    bouquet_query=Bouquet.objects.all()[:5]
    watch_query=Watch.objects.all()[:5]
    chocolate_query=Chocolate.objects.all()[:5]
    card_query=Card.objects.all()[:5]

    context={
        'cake':cake_query,
        'bouquet':bouquet_query,
        'watch':watch_query,
        'chocolate':chocolate_query,
        'card':card_query,
    }
    return render(request,"index.html",context)


# def sign_cust_page(request):
#     context={
#         "uname1":False,
#         "email1":False,
#         "pass1":False,
#         "email2":False
#     }
#     if request.POST:
#         name=request.POST.get("name")
#         email=request.POST.get("email")
#         username=request.POST.get("uname")
#         password=request.POST.get("psw")
#         confirm_pass=request.POST.get("cnfpsw")
#         phone=request.POST.get("phone")
#         qs=User.objects.filter(username=username)
#         qs1=User.objects.filter(email=email)
#         if qs.exists():
#             #username already exists
#             context={
#                 "uname1":True
#             }
#         elif qs1.exists():
#             #email already exists
#             context = {
#                 "email1": True
#             }
#         elif password!=confirm_pass:
#             #password not same
#             context = {
#                 "pass1": True
#             }
#         elif not ".com" in email:
#             context = {
#                 "email2": True
#             }
#         else:
#             new_user=User.objects.create_user(username=username,email=email,password=password)
#             cust_profile=Customer(
#                 name=name,
#                 email=email,
#                 username=username,
#                 phone=phone
#             )
#             cust_profile.save()
#             if new_user is not None:
#                 return redirect("/login")
#     return render(request,"auth/customer_signup.html",context)
#
#
# def sign_ret_page(request):
#     context = {
#         "uname1": False,
#         "email1": False,
#         "pass1": False,
#         "gstno1":False,
#         "aadhar1":False,
#         "email2": False
#     }
#     if request.POST:
#         firstname = request.POST.get("retailer_firstname")
#         lastname=request.POST.get("retailer_lastname")
#         email = request.POST.get("retailer_email")
#         username = request.POST.get("retailer_uname")
#         confirm_pass=request.POST.get("retailer_cnfpsw")
#         password = request.POST.get("retailer_psw")
#         phone = request.POST.get("retailer_phone")
#         address=request.POST.get("retailer_address")
#         gstno=request.POST.get("retailer_gstno")
#         aadhar=request.POST.get("retailer_aadhar")
#         qs = User.objects.filter(username=username)
#         qs1 = User.objects.filter(email=email)
#         qs2=Retailer.objects.filter(gstno=gstno)
#         qs3=Retailer.objects.filter(aadhar=aadhar)
#         if qs.exists():
#             # username already exists
#             context = {
#                 "uname1": True
#             }
#         elif qs1.exists():
#             # email already exists
#             context = {
#                 "email1": True
#             }
#         elif qs2.exists():
#             # gstno already exists
#             context = {
#                 "gstno1": True
#             }
#         elif qs3.exists():
#             # aadhar already exists
#             context = {
#                 "aadhar1": True
#             }
#         elif password != confirm_pass:
#             # password not same
#             context = {
#                 "pass1": True
#             }
#         elif not ".com" in email:
#             context = {
#                 "email2": True
#             }
#         else:
#             new_user=User.objects.create_user(username=username,email=email,password=password)
#             retail_profile = Retailer(
#                 firstname=firstname,
#                 lastname=lastname,
#                 email=email,
#                 username=username,
#                 phone=phone,
#                 address=address,
#                 gstno=gstno,
#                 aadhar=aadhar,
#             )
#             retail_profile.save()
#             if new_user is not None:
#                 return redirect("/login")
#     return render(request, "auth/retailer_signup.html", context)

def login_page(request):
    context={"b":False}
    if request.POST:
        username=request.POST.get("uname")
        password=request.POST.get("psw")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            c = Customer.objects.filter(username=username)
            print(c)
            login(request, user)
            if c!=[]:
                return redirect("/products")
            else:
                return redirect("/")
        else:
            #wrong credentials
            context={"b":True}
    return render(request,"auth/login.html",context)







