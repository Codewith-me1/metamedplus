from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import your custom user model

    # Customize the user admin as needed
    
# Register your custom user model with the admin si
# 
admin.site.register(CustomUser, UserAdmin)