from django.contrib import admin

# Register your models here.
#from.models import Employee,LoginAuth
from.models import*
admin.site.register((Employee,LoginAuth))