from django import forms
from .models import Order, DeliveryMethod, PayMethod
from django.core.validators import RegexValidator

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
                                 label='First name',
                                 widget= forms.TextInput(attrs={'class': 'bay_form', 'placeholder': 'Vadim'}))
    last_name = forms.CharField(required=True,
                                 label='Last name',
                                 widget= forms.TextInput(attrs={'class': 'bay_form', 'placeholder': 'Hudo'}))
    email = forms.EmailField(required=True,
                                 label='First name',
                                 widget= forms.EmailInput(attrs={'class': 'bay_form', 'placeholder': 'Phfi@gmail.com'}))
    phone = forms.CharField(required=False,
                                 label='Phone',
                                 validators=[RegexValidator(regex=r'^\+380\d{9}$', massage= 'Enter a valid  Ukraiene phone number .')],
                                 widget=forms.TextInput(attrs={'class': 'forms-input', 'plsceholder': '+380970000000'}))
    city = forms.CharField(required=True,
                                 label='City',
                                 widget= forms.TextInput(attrs={'class': 'bay_form', 'placeholder': 'Plzen'}))
    address= forms.CharField(required=True,
                                 label='address',
                                 widget= forms.TextInput(attrs={'class': 'bay_form', 'placeholder': 'street Majova 9'}))
    delivery_method = forms.ModelChoiceField(queryset=DeliveryMethod.objects.all(),
                                             label='Select delivery method',
                                             widget= forms.Select(attrs={'class': 'bay_form'}))
    pay_method = forms.ModelChoiceField(queryset=PayMethod.objects.all(),
                                             label='Select pay method',
                                             widget= forms.Select(attrs={'class': 'bay_form'}))
    contact_me = forms.BooleanField(label="Check this box if you'd like us to call you back.",
                                    widget=forms.CheckboxInput(attrs={'class': 'bay_form'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'city', 'address', 'delivery_method', 
                  'pay_method', 'contact_me']
        