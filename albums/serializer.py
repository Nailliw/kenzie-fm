from rest_framework import serializers


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


class AlbumSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    band_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    n_tracks = serializers.IntegerField()


class BandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    album_set = AlbumSerializer(many=True)
    tags = TagSerializer(many=True)
