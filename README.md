#Prerequisites

1) Install Python. Go to this site and download the latest version  https://www.python.org/downloads/. Run the setup. 
2) Create a virtual environment and Install Django. Go to official documentation for this 'https://docs.djangoproject.com/en/3.2/howto/windows/'

# Unicode-Tasks

Task 1.py  contains the task 1 and its bonus both  are in that file only

#Pokedex

Website has 6 urls namely:

1) Homepage 'home/' just to redirect you to whatever you wanna see
2) Types 'types/' here types are displayed by HttpsRessponse as requested (Feature: User can click on any type and will go to Single Type page of that type)
3) Single Type 'types/<str:s>/' here a list of all pokemons of a single type is displayed (Feature: User can click on any pokemon and will go to Single Pokemon page of that Pokemon)
4) Single Pokemon 'pokemon/<str:p>/' here list of all moves and their weight is displayed
5) Search 'search/' type in any type and user will be redirected to Single Type view and if user inputs a Pokemon name then it redirects to Single Pokemon and also registers that pokemon as caught.
   Also it creates an pokemon in the database where caught pokemon are registered.
6) Caught Pokemon 'caught/' here the list of all caught pokemon is displayed as a list and other things useful during a battle like total no of moves are displayed
   (Feature: user can click on the number of moves and will be redirected to the list of all moves which he can use during battles)
