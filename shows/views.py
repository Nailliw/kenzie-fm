from .models import Show
from albums.models import Band
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import ShowPermission
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
import ipdb
from .serializers import ShowSerializer, ShowViewsSerializer

# Create your views here.


class ShowView(APIView):
    # esse disponibiliza o request.user
    authentication_classes = [TokenAuthentication]
    # esse bloqueia o acesso casa o usuario nao apresente
    # o token
    permission_classes = [IsAuthenticated, ShowPermission]

    def get(self, request, band_id):
        band = get_object_or_404(Band, id=band_id)
        queryset = band.show_set.all()

        serializer = ShowSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, band_id):
        band = get_object_or_404(Band, id=band_id)

        serializer = ShowSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        show = Show.objects.create(**serializer.data, band=band)

        serializer = ShowSerializer(band)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# alterar quais pessoas tem permissão de assistir
class UpdateShowViewersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ShowPermission]

    def put(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)

        serializer = ShowViewsSerializer(data=request.data)

        ipdb.set_trace()
