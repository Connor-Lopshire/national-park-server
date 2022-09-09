from rest_framework import serializers
from ..models.reviews import Review

class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for Image"""
    class Meta:
        model = Review
        fileds = ('id', 'park_id', 'user_id', 'content')