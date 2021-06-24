from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializer import TagSerializer
from rest_framework import status
from ..models import Band, Tag


class TagCreateView(APIView):
    def post(self, request, band_id):
        band = get_object_or_404(Band, id=band_id)

        serializer = TagSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        tag = Tag.objects.create(**serializer.data)
        band.tags.add(tag)

        serializer = TagSerializer(tag)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
