from rest_framework import serializers
from albums.serializer import BandSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    band = BandSerializer(read_only=True)


class CredentialSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
