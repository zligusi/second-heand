from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm , UpdateForm 
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend= 'django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})