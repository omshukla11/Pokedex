from django.http import HttpResponse, Http404, response
from django.shortcuts import render
from django.template import context, loader, RequestContext, Template
import requests
import json

from requests.models import Request
# Create your views here.

url = 'https://pokeapi.co/api/v2/'
s1 = 'type/'
types_req = requests.get(url+s1)
if types_req.status_code == 200:
    data= json.loads(types_req.text)
    data_list = data['results']
    types = []
    for d in data_list:
        types.append(d['name'])

def types_view(request):
    template = Template('<title> Types of Pokemons </title> <h1>There are 20 types of pokemons namely:</h1> <h2> <ol> {% for t in types %} <li><a href="/types/{{ t }}">{{ t|capfirst }}</a></li> <br> {% endfor %} </ol> </h2>')
    context = RequestContext(request, {'types': types})
    return HttpResponse(template.render(context))
    # try:
    #     return render(request, 'types.html', {'types': types})
    # except types.DoesNotExist:
    #     raise Http404


def single_type_view(request, s):
    single_type_url = url + s1 + s
    single_type_req = requests.get(single_type_url)
    if single_type_req.status_code == 200:
        single_type_data = json.loads(single_type_req.text)
        pokemon_type = single_type_data['names'][-1]['name']
        pokemon_list = single_type_data['pokemon']
        all_pokemons = []
        for l in pokemon_list:
            all_pokemons.append(l['pokemon']['name'])

    return render(request, 'singletypes.html', {'type':pokemon_type, 'names':all_pokemons})

def search_view(request):
    if request.method == "GET":
        my_data = request.GET.get('type')
        my_data = str(my_data)
    return render(request, 'search.html',{})

def search_single_type(request):
    my_data = request.POST.get('type')
    context = {'data': my_data}
    return render(request, 'searchsingletype.html', context)
