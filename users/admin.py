from django.contrib import admin
from .models import CustomUser 


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'first_name', 'last_name', 
                    'is_staff', 'is_superuser']
    list_editable = ['is_staff', 'is_superuser']
    search_fields = ['email', 'phone', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_superuser']