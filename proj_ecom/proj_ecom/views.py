from django.http import HttpResponse
from django.contrib.auth import authenticate,login,get_user_model
from django.shortcuts import render,redirect

from customer_profile.models import Customer
from retailer_profile.models import Retailer



def sign_cust_page(request):
    