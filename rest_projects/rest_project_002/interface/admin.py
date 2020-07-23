from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('My_Requirements',{'fields': ('is_manager', 'department'),}),    
    )
# Register your models here.

admin.site.register(MyUser, UserAdmin)
