from django import forms

PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in renge(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOISES,
        coerce=int
    )
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    