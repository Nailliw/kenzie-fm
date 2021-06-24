from .models import Band, Album
from django.shortcuts import get_object_or_404


class BandService:
    @staticmethod
    def list_all_bands():
        return Band.objects.all()

    @staticmethod
    def create_album_for_band(album_data, band):
        return Album.objects.create(**album_data, band=band)
