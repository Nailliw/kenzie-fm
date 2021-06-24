from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializer import AlbumSerializer, BandSerializer, TagSerializer
from rest_framework import status
from ..models import Band, Album, Tag
from ..services import BandService


class BandListCreateView(APIView):
    def get(self, request):
        queryset = BandService.list_all_bands()
        serializer = BandSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BandSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        album_set = data.pop("album_set")
        tags = data.pop("tags")
        band = Band.objects.create(**data)

        for album in album_set:
            BandService.create_album_for_band(album, band)

        for tag in tags:
            tag = Tag.objects.create(**tag)
            # tag.bands.add(band)
            band.tags.add(tag)

        serializer = BandSerializer(band)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
