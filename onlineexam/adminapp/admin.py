from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(User)
admin.site.register(category)
admin.site.register(examtype)
admin.site.register(exam)
admin.site.register(Result)