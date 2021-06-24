from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializer import BandSerializer
from rest_framework import status
from ..models import Band, Tag


class BandRetrieveUpdateView(APIView):
    def get(self, request, band_id):
        band = get_object_or_404(Band, id=band_id)
        serializer = BandSerializer(band)

        return Response(serializer.data)

    def put(self, request, band_id):
        serializer = BandSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        band = Band.objects.get(id=band_id)

        data = serializer.data
        new_tags = data.pop("tags")
        old_tags = band.tags.all()

        #  aqui eu busco todas as tags antigas,  e por meio de um
        # list comprehension eu deleto as tags que não estão na variável new_tags
        for tag in old_tags:
            if tag.name not in [new_tag["name"] for new_tag in new_tags]:
                band.tags.remove(tag)

        for new_tag in new_tags:
            try:
                tag = Tag.objects.get(**new_tag)
                if tag and tag not in band.tags.all():
                    band.tags.add(tag)
            except ObjectDoesNotExist:
                tag = Tag.objects.create(**new_tag)
                band.tags.add(tag)

        serializer = BandSerializer(band)
        return Response(serializer.data)

    def delete(self, request, band_id):
        band = get_object_or_404(Band, id=band_id)
        band.delete()
        return Response(status.HTTP_NO_CONTENT)
