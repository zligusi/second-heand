from django.contrib import admin
from .models import Category , Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('photo', 'product_name', 'slug', 'description', 
    'quantity', 'price', )
    prepopulated_fields = {'slug': ('product_name,')}