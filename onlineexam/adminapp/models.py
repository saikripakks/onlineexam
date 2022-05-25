from re import M
from django.db import models
from userapp.models import *
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.hashers import make_password
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not email:
            raise ValueError('An Email address must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **other_fields)


class User(AbstractUser):

    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=30,null=True)
    phone=models.IntegerField(null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS  = ['phone']   
    objects=UserManager()

    def get_username(self):
        return self.email
    
class category(models.Model):
    subject=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.subject
class examtype(models.Model):
    type=models.CharField(max_length=20,null=True)
    no=models.IntegerField(null=True)
    time=models.IntegerField(null=True)
    start=models.DateTimeField(null=True)
    end=models.DateTimeField(null=True)
    cname=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.type 
class exam(models.Model):
    marks=models.IntegerField(null=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    examtype=models.ForeignKey(examtype,on_delete=models.CASCADE,null=True)
    question=models.CharField(max_length=1000,null=True)
    option1=models.CharField(max_length=200,null=True)
    option2=models.CharField(max_length=200,null=True)
    option3=models.CharField(max_length=200,null=True)
    option4=models.CharField(max_length=200,null=True)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)


class Result(models.Model):
    student = models.ForeignKey(candidate,on_delete=models.CASCADE)
    category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    exam = models.ForeignKey(examtype,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

