from rest_framework import serializers

from nationalparkapi.models.parks import Park
from nationalparkapi.serializers.image import ImageSerializer

class ParkSerializer(serializers.ModelSerializer):
    """JSON serializer for main park list and bucket list"""
    images = ImageSerializer(many=True)
    class Meta:
        model = Park
        fields = ('id', 'images', 'full_name')