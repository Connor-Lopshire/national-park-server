from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """serializer for User """
    class Meta:
        model = User
        fields= ('id', 'username')