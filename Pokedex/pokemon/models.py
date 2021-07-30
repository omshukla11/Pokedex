from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

# Create your models here.

class Poke_class(models.Model):
    poke_name    = models.TextField()
    poke_type    = models.TextField()
    front_url    = models.URLField(blank=True, null=True)
    back_url     = models.URLField(blank=True, null=True)
    weight       = models.FloatField()
    totmoves     = models.IntegerField(default=0)

    def __str__(self):
        return self.poke_name

    def get_remote_image(self):
        if self.image_url and not self.image_file:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.image_file.save(f"image_{self.pk}", File(img_temp))
        self.save()