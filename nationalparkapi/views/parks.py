
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nationalparkapi.models.parks import Park
from nationalparkapi.models.visited_parks import VisitedPark
from nationalparkapi.serializers.park import DetailedParkSerializer, ParkSerializer
from rest_framework.decorators import action

from nationalparkapi.serializers.visited_park import VisitedParkSerializer

class ParkView(ViewSet):
    def list(self, request):
        """list of all parks"""

        parks = Park.objects.all()
        serializer = ParkSerializer(parks, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        """method to get single park with reviews and more details"""
        park = Park.objects.get(pk=pk)
        serializer = DetailedParkSerializer(park)
        return Response(serializer.data, status= status.HTTP_200_OK)
    @action(methods=['get'], detail=False)
    def bucket_list_parks(self, request):
        parks = request.auth.user.bucket_list_parks.all()
        serializer = ParkSerializer(parks, many=True)
        return Response(serializer.data)
    @action(methods=['post'], detail=True)
    def add_bucket_list(self, request,pk):
        park = Park.objects.get(pk=pk)
        request.auth.user.bucket_list_parks.add(park.id)
        return Response(status= status.HTTP_201_CREATED)
    @action(methods=['get'], detail=False)
    def visited_parks(self, request):
        parks = request.auth.user.visited_parks.all()
        serializer = VisitedParkSerializer(parks, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    @action(methods=['post'], detail=True)
    def add_park_visit(self, request, pk):
        park = Park.objects.get(pk=pk)
        VisitedPark.objects.update_or_create(
            park = park,
            user = request.auth.user,
            date = request.data['date']
        )
        return Response(None, status= status.HTTP_201_CREATED)