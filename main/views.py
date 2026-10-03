from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Products 

def home(request):
    top_products = Products.objects.filter(is_top=True)[:8]
    products = Products.objects.all()
    return render(request, 'main/home.html', {'products': products, 'top_products': top_products})

