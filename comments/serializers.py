from rest_framework import serializers
from comments.models import Comments


class CommentCreateSerializer(serializers.Serializer):
    csv_file = serializers.FileField()


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'