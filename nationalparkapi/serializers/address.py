from rest_framework import serializers
from ..models.addresses import Address

class AddressSerializer(serializers.ModelSerializer):
    """JSON serializer for Image"""
    class Meta:
        model = Address
        fileds = ('id', 'park_id', 'city', 'state_code')