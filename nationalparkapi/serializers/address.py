from rest_framework import serializers
from ..models.addresses import Address

class AddressSerializer(serializers.ModelSerializer):
    """JSON serializer for Address"""
    class Meta:
        model = Address
        fields = ('id', 'park_id', 'city', 'state_code')