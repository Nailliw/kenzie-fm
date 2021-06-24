from django.db import models
from albums.models import Band
from authentication.models import User

# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=255)

    # desse jeito ficaria band.shows
    # band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name="shows")

    # desse jeito fica band.show_set
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    viewers = models.ManyToManyField(User, related_name="shows")
