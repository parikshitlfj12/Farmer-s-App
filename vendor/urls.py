"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('dashboard/', views.dashboard),
    path('orders/', views.orders),
    path('products/', views.products),
    path('coupons/', views.coupons),
    path('aboutme/', views.aboutme),
    path('chart/', views.chart),
    path('table/', views.table),
    path('products/add-new-products/',views.add_new_product),
    path('coupons/add-new-coupon/', views.add_new_coupon)
]
