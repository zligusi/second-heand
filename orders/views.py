from django.shortcuts import render, get_object_or_404
from .form import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form =  OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart :
                OrderCreateForm.objects.create(order=order,
                                               product=item['product'],
                                               price=item['price'],
                                               quantity=item['quantity'])
                cart.clear()
            return render(request, 'orders/create.html', {'order': order})
    else:
        form = OrderCreateForm()
        return render (request, 'orders/create.html', {'cart': cart, 
                                                       'form': form })



