from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

# Create your models here.

class Poke_class(models.Model):
    poke_name    = models.TextField()
    poke_type    = models.TextField()
    no_poke      = models.IntegerField(default=1)
    front_url    = models.URLField(blank=True, null=True)
    back_url     = models.URLField(blank=True, null=True)
    weight       = models.FloatField()
    totmoves     = models.IntegerField(default=0)

    def __str__(self):
        return self.poke_name