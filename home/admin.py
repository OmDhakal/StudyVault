from django.contrib import admin

from .models import UserRegister


# Register your models here.
class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password")
