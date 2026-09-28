from django.contrib import admin
from .models import Category , Size,  Products, \
    ProductImage, ProductSize

class ProductsImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 

class ProductSizeInline(admin.TabularInline):
    model = Size
    extra = 1 


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'color', 'price']
    list_filter = ['category', 'color']
    search_fields = ['name', 'color', 'description']
    prepopulated_fields = {'slug':('name',)}
    inlines = [ProductsImageInline, ProductSizeInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Products, ProductsAdmin)