from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('loginpage',loginuser,name='login'),
    path('cat',addcategorypage,name='addcat'),
    path('examtype',addexamtypepage,name='addexamtype'),
    path('register',register,name='reg'),
    path('exam',addexampage,name='addexam'),

]