from rest_framework import serializers


class MostAverageRatingMoviesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    language = serializers.CharField(max_length=10, read_only=True)
    averageRating = serializers.FloatField(read_only=True)
    titleID = serializers.CharField(max_length=100)
    numVotes = serializers.IntegerField()
