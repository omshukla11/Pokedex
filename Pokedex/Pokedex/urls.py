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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pokemon.views import home_view, mytype_view, searchedpokemon, single_pokemon_view, types_view, single_type_view, search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='HomePage'),
    path('types/', types_view, name='Types of Pokemon'),
    path('mytypes/', mytype_view, name='Types of Pokemon'),
    path('types/<str:s>/', single_type_view, name='Pokemon'),
    path('pokemon/<str:p>/', single_pokemon_view, name='PokemonInfo'),
    path('search/', search_view, name='SearchPokemon'),
    path('searched/', searchedpokemon, name='SearchedPokemon')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)