from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Products 

def home(request):
    top_products = Products.objects.filter(is_top=True)[:8]
    products = Products.objects.all()
    return render(request, 'main/home.html', {'products': products, 'top_products': top_products})


def product_detail(request, id, slug):
    product = get_object_or_404(Products, id=id, slug=slug,)
    related_products = Products.objects.filter(category=product.category, 
                                               ).exclude(id=product.id)[:3]
    
    if product.stock >= 0 :
      raise Http404("i'm not have this product")

    return render(request, 'main/produc_detail.html', {'product': product,
                                                       'related_products': related_products})

def about(request):
   return render(request, 'main/about.html' )