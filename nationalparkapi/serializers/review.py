from rest_framework import serializers

from nationalparkapi.serializers.users import UserSerializer
from ..models.reviews import Review

class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for Image"""
    user = UserSerializer()
    class Meta:
        model = Review
        fields = ('id', 'park_id', 'user_id', 'content', 'user')