from django import forms
from django .contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django.utils.html import strip_tags
from django.core.validators import RegexValidator


User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, 
                             widget=forms.EmailInput(attrs={'class': 'forms-input', 'placeholder': 'Enter your email .'}))
    first_name = forms.CharField(required=True, 
                                 widget=forms.TextInput(attrs={'class': 'forms-input', 'placeholder': 'Enter your first name .'}))
    last_name = forms.CharField(required=True, 
                                     widget=forms.TextInput(attrs={'class': 'forms-input', 'placeholder': 'Enter your last name .'}))
    password1 = forms.CharField(required=True, 
                                widget=forms.PasswordInput(attrs={'class': 'forms-imput', 'placeholder': 'Enter your password .'}))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'forms-imput', 'placeholder': 'Confirm your password .'}))


    class Meta:
        model = User 
        fields = ('email', 'first_name', 'lsat_name', 'password1', 'password2')


    def clean_email(self):
        email= self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use .')
        return email


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user 


class LoginForm(AuthenticationForm):
    # username = email because in models.py 
    # USERNAME_FIELD = 'email'
    username = forms.CharField(label='Email',
                               widget=forms.EmailInput(attrs={'class': 'forms-input','authofocus': True, 'placeholder': 'Enter your email .'}))
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(attrs={'class': 'forms-input', 'authofocus': True, 'placeholder': 'Enter your password .'}))


    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password :
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Invalid Email or password .')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('This accoutn is inactive .')
        return self.cleaned_data


class UpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, 
                            label='Email',
                            widget=forms.EmailInput(attrs={'class': 'forms-input', 'placeholder': 'Tort24abcd@gmail.com'})
                            )
    phone = forms.CharField(required=False,
                            label='Phone',
                            validators=[RegexValidator(regex=r'^\+380\d{9}$', massage= 'Enter a valid  Ukraiene phone number .')],
                            widget=forms.TextInput(attrs={'class': 'forms-input', 'plsceholder': '+380970000000'})
                            )
    first_name = forms.CharField(required=True,
                                label='First_name',
                                widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Walter'})
                                )
    last_name = forms.CharField(required=True,
                                    label='Last_name',
                                    widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'White'})
                                )
    city = forms.CharField(required=False,
                           label='City',
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Albuquerque'})
                           )
    address = forms.CharField(required=False,
                              label='Address',
                              widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Negra Arroyo Lane 308'})
                            )
    nova_post = forms.CharField(required=False,
                                label='Nova-poshta branch number',
                                widget=forms.TextInput(attrs={'classs': 'form-input', 'placeholder': 'Branch #1, Kyiv, Pyrohivskyi Shliakh 135 | Branch #1 '})
                                )


    class Meta:
        model = User 
        field = ('email', 'phone', 'first_name', 'last_name', 'city', 'address', 'nova_post')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('This email is already in use .')
        return email 

    def clean(self):
        cleaned_data =  super().clean()
        if not cleaned_data.get('email'):
            cleaned_data['email'] = self.instance.email 

            for field in ['phone', 'first_name', 'last_name', 'city', 'address', 'nova_post']:
                if cleaned_data.get(field):
                    cleaned_data[field]= strip_tags(cleaned_data[field])

                return cleaned_data  