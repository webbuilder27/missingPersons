from django.contrib import admin
from .models import MissingPerson
# Register your models here.
#This allows our admin site to register our MissingPerson class and add it to our table.

admin.site.register(MissingPerson)