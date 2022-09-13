from collections import UserDict
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action

from nationalparkapi.models.parks import Park
from nationalparkapi.models.reviews import Review


class ReviewView(ViewSet):
    @action(methods=['post'], detail=True)
    def add_review(self, request, pk):
        """method for creating a park review"""
        park = Park.objects.get(pk=pk)
        Review.objects.create(
            park = park,
            user = request.auth.user,
            content = request.data['content']
        )
        return Response(None, status=status.HTTP_201_CREATED)
    @action(methods=['delete'], detail=True)
    
    def delete_review(self, request, pk):
        Review.objects.get(pk=pk).delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
