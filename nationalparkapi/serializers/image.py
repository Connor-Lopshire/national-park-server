from rest_framework import serializers
from ..models.images import Image

class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for Image"""
    class Meta:
        model = Image
        fileds = ('id', 'park_id', 'credit', 'title', 'alt_text',' caption', 'url')