from django.db import models


class candidate(models.Model):
    email=models.EmailField(max_length=100,unique=True)
    name=models.CharField(max_length=100,)
    password=models.CharField(max_length=20)
    phone=models.CharField(max_length=100)
    def __str__(self):
        return self.email