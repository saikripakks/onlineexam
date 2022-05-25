from django.shortcuts import render
from .models import *
from adminapp.models import *
import pandas as pd
import os
from pathlib import Path
from django.contrib.auth import logout, authenticate, login
from django.http.response import HttpResponse
BASE_DIR = Path(__file__).resolve().parent.parent
from django.core.files import File
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method=="POST":
        em=request.POST.get("email")
        p=request.POST.get("password")
        User.objects.create_user(email=em, password=p)
    return render(request,"user/reg.html")
def loginuser(request):
    if request.method=="POST":
        em=request.POST.get("email")
        pw=request.POST.get("password")
        user=authenticate(request,email=em, password=pw)
        if user:
            login(request,user)
            return render(request,"user/index.html")
        else:
            return render(request,"user/login.html")

    return render(request,"user/login.html")
# Create your views here.
@login_required
def indexpage(request):
    data=category.objects.all()
    return render(request,"user/index.html",{'data':data})
def courseviewpage(request,userid):
    dat=examtype.objects.all()
    return render(request,"user/courseview.html", {'dat':dat})
def examviewpage(request,userid):
    data=exam.objects.filter()
    return render(request,"courseview.html", {'data':data})