from rest_framework import serializers


class IMDBFileCreateSerializer(serializers.Serializer):
    csv_file = serializers.FileField()


class IMDBMoviesListSerializer(serializers.Serializer):
    titleId = serializers.CharField(max_length=25)
    title = serializers.CharField(max_length=500)
    language = serializers.CharField(max_length=10)
