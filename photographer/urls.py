"""
URL configuration for photographer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('about-me/',views.about_me_view, name='about_me'), 
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('travel/', views.travel_view, name='travel'),
    path('street/', views.street_view, name='street'),
    path('landscape/', views.landscape_view, name='landscape'),
    path('portrait/', views.portrait_view, name='portrait')
]
