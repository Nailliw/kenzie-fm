from .models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, CredentialSerializer


class UserView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # se usarmos serializer.data -> NÃO TEM PASSWORD
        # o hash da password só acontece porque nós usamos
        # User.objects.create_user
        user = User.objects.create_user(
            username=request.data["username"], password=request.data["password"]
        )

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProtectedCiew(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"user": request.user.username, "authenticated": True})


class LoginView(APIView):
    def post(self, request):
        serializer = CredentialSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=request.data["username"], password=request.data["password"]
        )

        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({"token": token.key})

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
