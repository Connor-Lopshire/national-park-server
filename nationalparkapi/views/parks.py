
from re import search
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nationalparkapi.models.parks import Park
from nationalparkapi.models.states import State
from nationalparkapi.models.visited_parks import VisitedPark
from nationalparkapi.serializers.park import DetailedParkSerializer, ParkSerializer
from rest_framework.decorators import action
from nationalparkapi.serializers.state import StateSerializer
from nationalparkapi.serializers.users import UserSerializer
from rest_framework.pagination import LimitOffsetPagination
from nationalparkapi.serializers.visited_park import VisitedParkSerializer

class ParkView(ViewSet):
    pagination_class = LimitOffsetPagination
    def list(self, request):
        """list of all parks"""

        parks = Park.objects.all()
        search_term = request.query_params.get('q', None)
        state_query = request.query_params.get('state', None)
        if search_term != '' and search_term is not None:
            parks = parks.filter(full_name__icontains = search_term).distinct()
        if state_query != '' and state_query is not None:
            parks =parks.filter(state__icontains = state_query).distinct()
        for park in parks:
            park.visited = request.auth.user
            park.in_bucket = request.auth.user
        pagination = LimitOffsetPagination()
        parks_pag = pagination.paginate_queryset(parks, request)
        serializer = ParkSerializer(parks_pag, many=True)
        return pagination.get_paginated_response(serializer.data)
    

    def retrieve(self, request, pk):
        """method to get single park with reviews and more details"""
        park = Park.objects.get(pk=pk)
        park.visited = request.auth.user
        park.in_bucket = request.auth.user

        serializer = DetailedParkSerializer(park)
        for review in serializer.data['reviews']:
            review['author'] = True if review['user']['id'] == request.auth.user.id else False
        
        return Response(serializer.data, status= status.HTTP_200_OK)
    @action(methods=['get'], detail=False)
    def bucket_list_parks(self, request):
        parks = request.auth.user.bucket_list_parks.all()
        for park in parks:
            park.visited = request.auth.user
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
        user_serializer = UserSerializer(request.auth.user)
        for park in serializer.data:
            park['park']['visited'] = True if park['user'] == user_serializer.data else False
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
    @action(methods=['delete'], detail=True)
    def remove_bucket_list(self, request, pk):
        request.auth.user.bucket_list_parks.remove(pk)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    @action(methods=['delete'], detail=True)
    def remove_visit(self, request, pk):
        visited_park = VisitedPark.objects.get(pk=pk)
        visited_park.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    @action(methods=['get'], detail=False)
    def get_states(self, request):
        states = State.objects.all()
        serializer = StateSerializer(states,many=True)

        return Response(serializer.data)