
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nationalparkapi.models.parks import Park
from nationalparkapi.models.visited_parks import VistedPark
from nationalparkapi.serializers.park import ParkSerializer
from rest_framework.decorators import action

class ParkView(ViewSet):
    def list(self, request):
        """list of all parks"""

        parks = Park.objects.all()
        serializer = ParkSerializer(parks, many=True)
        return Response(serializer.data)
    @action(methods=['get'], detail=False)
    def bucket_list_parks(self, request):
        parks = request.auth.user.bucket_list_parks.all()
        serializer = ParkSerializer(parks, many=True)
        return Response(serializer.data)
    @action(methods=['post'], detail=True)
    def add_bucket_list(self, request,pk):
        park = Park.objects.get(pk=pk)
        new_bucket_list_park = request.auth.user.bucket_list_parks.add(park.id)
        serializer = ParkSerializer(new_bucket_list_park)
        return Response(status= status.HTTP_201_CREATED)
    @action(methods=['get'], detail=False)
    def visited_parks_list(self, request):
        parks = request.auth.user.visited_parks.all()
        serializer = ParkSerializer(parks, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    @action(methods=['post'], detail=False)
    def visited_park(self, request):
        park = VistedPark.objects.create(

        )
        serializer = ParkSerializer(park)
        return Response(serializer.data, status= status.HTTP_201_CREATED)