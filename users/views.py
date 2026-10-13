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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend= 'django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


@login_required
def account_detail(request):
    return render(request, 'users/account_detail.html', {'user': request.user})


@login_required 
def update_account(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.clean()
            return redirect(request, 'users:account_detail')
    else:
        form = UpdateForm(instance=request.user)
    return render(request, 'users/update_account.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('register')