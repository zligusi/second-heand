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
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})


@login_required
def account_detail(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, 'users/account_detail.html', {'user': user})


@login_required
def edit_account_detail(request):
    form = UpdateForm(instance=request.user)
    return render(request, 'users/edit_account_detail.html', {'form': form, 'user': request.user})


@login_required
def update_account_detail(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.clean()
            user.save()
            return redirect('users:account_detail', {'user': user})
        else: 
            return render(request, 'users/update_acount.html', {'user': request.user})  
    return redirect('users:profile', {'user': user})


def logout_view(request):
    logout(request)
    return redirect('register')