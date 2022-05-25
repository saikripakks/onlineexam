from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',indexpage,name='index'),
    path('<int:userid>',courseviewpage,name='index'),
    path('exam <int:userid>',examviewpage,name='index'),
    path('loginuser',loginuser,name='logi'),
    path('reg',register,name='regi'),
]