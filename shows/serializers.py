from rest_framework import serializers
from albums.serializer import BandSerializer
from authentication.serializers import UserSerializer
from authentication.models import User


class ShowSerializer(serializers.Serializer):
    name = serializers.CharField()
    band = BandSerializer(read_only=True)
    viewers = UserSerializer(read_only=True, many=True)


class ShowViewsSerializer(serializers.Serializer):
    viewers_ids = serializers.ListField(child=serializers.IntegerField())

    def validate_viewers_ids(self, value):
        for user_id in value:
            if user_id not in [user.id for user in User.objects.all()]:
                raise serializers.ValidationError("user nor found")

        return value
