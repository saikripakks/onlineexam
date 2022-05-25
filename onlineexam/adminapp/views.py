from click import option
from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.http.response import HttpResponse
from .models import *
# Create your views here.

def register(request):
    if request.method=="POST":
        em=request.POST.get("email")
        p=request.POST.get("password")
        User.objects.create_user(email=em, password=p)
    return render(request,"admin/reg.html")
def loginuser(request):
    if request.method=="POST":
        em=request.POST.get("email")
        pw=request.POST.get("password")
        user=authenticate(request,email=em, password=pw)
        if user:
            login(request,user)
            return render(request,"admin/index.html")
        else:
            return render(request,"admin/login.html")

    return render(request,"admin/login.html")

def addcategorypage(request):

    if request.method=="POST":
        sub=request.POST.get('sub')

        category.objects.create(subject=sub)
        return HttpResponse("Data added")
    return render (request,"admin/index.html")

def addexamtypepage(request):
    k=category.objects.all()
    if request.method=="POST":
        ty=request.POST.get('type')
        no=request.POST.get('no')
        t=request.POST.get('time')
        s=request.POST.get('start')
        e=request.POST.get('end')
        ca=request.POST.get('catg')
        cat=category.objects.get(subject=ca)
        examtype.objects.create(type=ty,no=no,time=t,start=s,end=e,cname=cat)
        return HttpResponse("Data added")
    return render (request,"admin/addexamtype.html",{"cat":k})
def addexampage(request):
    k=category.objects.all()
    k1=examtype.objects.all()
    if request.method=="POST":
        m=request.POST.get('marks')
        q=request.POST.get('question')
        o1=request.POST.get('option1')
        o2=request.POST.get('option2')
        o3=request.POST.get('option3')
        o4=request.POST.get('option4')
        ans=request.POST.get('answer')
        ca=request.POST.get('catg')
        cat=category.objects.get(subject=ca)
        ex=request.POST.get('type')
        exa=examtype.objects.get(type=ex)
        exam.objects.create(marks=m,category=cat,examtype=exa,question=q,option1=o1,option2=o2,option3=o3,option4=o4,answer=ans)
        return HttpResponse("Data added")
    return render (request,"admin/addexam.html",{"cat":k,'exam':k1})
