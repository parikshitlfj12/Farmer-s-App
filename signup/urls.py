from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path("signup/register", views.register, name="register"),
    path('signup/login', views.login, name='login'),
    path('signup/logout', views.logout, name='logout'),
    
    
    ]