from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('account_detail/', views.account_detail, name='account_detail'),
    path('edit_account_detail/', views.edit_account_detail, name='edit_account_detail'),
    path('update_account_detail/', views.update_account_detail, name='update_account_detail'),
    path('logout/', views.logout_view, name='logout'),
]