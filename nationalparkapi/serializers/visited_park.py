from rest_framework import serializers

from nationalparkapi.models.visited_parks import VisitedPark
from nationalparkapi.serializers.park import ParkSerializer
class VisitedParkSerializer(serializers.ModelSerializer):
    """JSON serializer for visited park data structure """
    park = ParkSerializer()
    class Meta:
        model = VisitedPark
        fields = ('id', 'date', 'park')