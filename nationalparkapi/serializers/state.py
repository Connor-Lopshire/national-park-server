from rest_framework import serializers

from nationalparkapi.models.states import State



class StateSerializer(serializers.ModelSerializer):
    """JSON serializer for states"""
    class Meta:
        model = State
        fields = ('id', 'state_code')