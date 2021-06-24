from django.db import models

from django.contrib.auth.models import AbstractUser
from albums.models import Band


class User(AbstractUser):
    band = models.ForeignKey(
        Band, on_delete=models.CASCADE, default=None, blank=True, null=True
    )
