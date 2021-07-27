from django.db import models

# Create your models here.

class Pokeclass():
    name         = models.TextField()
    poke_type    = models.TextField()
    sprites      = models.ImageField()
    height       = models.FloatField()
    moves        = models.TextField()
    totabilities = models.IntegerField()