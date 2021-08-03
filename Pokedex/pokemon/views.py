from pokemon.models import Poke_class
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.template import RequestContext, Template, context
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
    template = Template('{% extends "navbar.html" %}<head><title> Types of Pokemons </title></head>{% block content %}<div class="bg-image"><div class="poke-text"><h1>There are 20 types of pokemons namely:</h1><h2><ol>{% for t in types %}<li><a href="/types/{{ t }}">{{ t|capfirst }}</a></li><br>{% endfor %}</ol></h2></div></div>{% endblock %}')
    context = RequestContext(request, {'types': types})
    return HttpResponse(template.render(context))

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
    p = str(p)
    poke_url = url + 'pokemon/' + p
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
                'name': p,
                'frontpic': front_pic,
                'backpic': back_pic,
                'moves': moves,
                'weight': weight
        }
        totmoves = len(poke_data["moves"])
        poke_type = ""
        for t in poke_data['types']:
            poke_type += t['type']['name']
            if t!=poke_data['types'][-1]:
                poke_type += ", "

        caught_poke = {
                'poke_name': p,
                'poke_type': poke_type,
                'front_url': front_pic,
                'back_url': back_pic,
                'weight': weight,
                'totmoves': totmoves
        }
        if (Poke_class.objects.filter(poke_name=p).exists()):
            obj=Poke_class.objects.get(poke_name=p)
            obj.no_poke += 1
            obj.save()
        else:
            Poke_class.objects.create(**caught_poke)
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

def caught_view(request):
    poke_set = Poke_class.objects.all()
    context = {'poke': poke_set}
    return render(request, 'caught.html', context)