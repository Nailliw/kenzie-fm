from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializer import AlbumSerializer
from rest_framework import status
from ..models import Band
from ..services import BandService

# Create your views here.


class AlbumCreateView(APIView):
    def post(self, request, pk):
        band = get_object_or_404(Band, id=pk)
        serializer = AlbumSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        album = BandService.create_album_for_band(serializer.data, band)
        serializer = AlbumSerializer(album)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
