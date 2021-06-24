from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.serializers import UserSerializer
from authentication.models import User
from rest_framework import status
from ..models import Band


# Create your views here.


class BandMemberView(APIView):
    def post(self, request, band_id):
        band = get_object_or_404(Band, id=band_id)

        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            **serializer.data, password=request.data["password"], band=band
        )

        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)
