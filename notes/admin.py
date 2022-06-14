from django.contrib import admin
from .models import *
from notes.models import Signup
# Register your models here.
admin.site.register(Signup)
admin.site.register(Notes)