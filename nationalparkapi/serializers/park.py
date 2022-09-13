from dataclasses import fields
from rest_framework import serializers

from nationalparkapi.models.parks import Park
from nationalparkapi.serializers.address import AddressSerializer
from nationalparkapi.serializers.image import ImageSerializer
from nationalparkapi.serializers.review import ReviewSerializer

class ParkSerializer(serializers.ModelSerializer):
    """JSON serializer for main park list and bucket list"""
    images = ImageSerializer(many=True)
    class Meta:
        model = Park
        fields = ('id', 'images', 'full_name', 'state')

class DetailedParkSerializer(serializers.ModelSerializer):
    """serializer for detailed park view including images and address and reviews"""
    images = ImageSerializer(many=True)
    addresses = AddressSerializer(many = True)
    reviews = ReviewSerializer(many = True)
    class Meta:
        model = Park
        fields = ('id', 'images', 'addresses', 'reviews', 'url', 'full_name', 'description', 'designation')  

