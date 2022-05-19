from rest_framework import serializers
from comments.models import Comments


class CommentCreateSerializer(serializers.Serializer):
    csv_file = serializers.FileField()


class CommentListSerializer(serializers.ModelSerializer):
    review = serializers.CharField(max_length=500000, read_only=True)
    sentiment = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'