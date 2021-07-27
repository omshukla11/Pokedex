from django.urls import re_path
from pokemon.views import single_type_view

app_name = 'Pokemon'

urlpatterns = [
    re_path(r'$', single_type_view, name='SearchedPokemon')
]