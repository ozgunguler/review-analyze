from rest_framework import serializers


class IMDBRatingsListSerializer(serializers.Serializer):
    tconst = serializers.CharField(max_length=25)
    averageRating = serializers.FloatField()
    numVotes = serializers.IntegerField()
