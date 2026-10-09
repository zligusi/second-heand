from django.db import models
from main.models import Product


class DeliveryMethod(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

class PayMethod(models.Model):
    name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    def __str__(self):
            return str(self.name)

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.PROTECT )
    pay_method = models.ForeignKey(PayMethod, on_delete=models.PROTECT)
    buy_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    contact_me = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ['-buy_date',]
        indexes = [
            models.Index(fields=['-buy_date',]),
        ]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", 
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", 
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


    def get_cost(self):
        return self.price * self.quantity
