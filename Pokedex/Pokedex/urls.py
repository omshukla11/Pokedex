"""Pokedex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from django.urls.conf import include
from pokemon.views import types_view, single_type_view, search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('types/', types_view, name='Types of Pokemon'),
    path('types/<str:s>/', single_type_view, name='Pokemon'),
    re_path('search/', search_view, name='Search the type of Pokemon'),
    re_path(r'search/<str:s>', include('pokemon.urls',namespace='Pokemon'), name='SearchedPokemon')
]
