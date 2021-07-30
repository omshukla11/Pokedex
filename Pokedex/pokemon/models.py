from django.db import models

# Create your models here.

class Poke_class(models.Model):
    poke_name    = models.TextField()
    poke_type    = models.TextField()
    weight       = models.FloatField()
    moves        = models.TextField()
    totabilities = models.IntegerField()