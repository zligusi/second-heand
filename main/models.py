from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)


    def  save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=25)

    def __str__ (self):
        return self.size
    

class ProductSize(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, 
                                related_name='product_size')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)


    def  __str__(self):
        return F"{self.size.name} ({self.stock} in stock) for {self.product.name}"


class Products(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    photo = models.ImageField(upload_to='products_photo/main', blank=True, null=True)
    name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                  related_name='products')
    defects = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)


    def  save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, 
                                related_name='images')
    image = models.ImageField(upload_to='products/extra/main')