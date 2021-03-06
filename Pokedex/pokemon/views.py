from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.template import RequestContext, Template
import requests
import json

from requests.models import Request
# Create your views here.

def home_view(request):
    return render(request, 'homepage.html', {})

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

def mytype_view(request):
    try:
        return render(request, 'types.html', {'types': types})
    except types.DoesNotExist:
        raise Http404

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
    else:
        raise Http404


    
def single_pokemon_view(request, p):
    poke_url = url + 'pokemon/' + str(p)
    poke_req = requests.get(poke_url)
    if poke_req.status_code == 200:
        poke_data = json.loads(poke_req.text)
        front_pic = poke_data['sprites']['front_default']
        back_pic = poke_data['sprites']['back_default']
        weight = poke_data['weight'] 
        moves = []
        for m in poke_data["moves"]:
            moves.append(m["move"]["name"])
        context = {
                'name': str(p),
                'frontpic': front_pic,
                'backpic': back_pic,
                'moves': moves,
                'weight': weight
        }
        return render(request, 'singlepoke.html', context)
    else:
        raise Http404
    
def search_view(request):
    if request.method == "GET":
        my_data = request.GET.get('type')
        my_data = str(my_data)
    return render(request, 'search.html',{})

def searchedpokemon(request):
    t = request.POST['search']
    if t in types:
        return redirect('/types/'+t)
    else:
        try:
            return redirect('/pokemon/'+t)
        except:
            raise Http404
