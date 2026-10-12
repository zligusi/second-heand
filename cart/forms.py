from django import forms

PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in renge(1, 21)]

class CartAddProductForm(forms.Form):
    pass