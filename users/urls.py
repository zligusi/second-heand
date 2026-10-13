from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('account_detail/', views.account_detail, name='account_detail'),
    path('update_account/', views.update_account, name='update_account'),
    path('logout/', views.logout_view, name='logout'),
]