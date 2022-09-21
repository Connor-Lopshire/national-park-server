
from urllib import response
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nationalparkapi.models.parks import Park
from nationalparkapi.models.images import Image
from nationalparkapi.models.addresses import Address


from nationalparkapi.serializers.park import ParkSerializer
from rest_framework.decorators import action
import requests
import os
class DataCollectionView(ViewSet):
    @action(methods=['get'], detail=False) 
    def get_national_parks(self, request):
        Park.objects.all().delete()
        

        url = f'https://developer.nps.gov/api/v1/parks?limit=468&api_key={os.environ.get("MY_API_KEY")}'
        response = requests.get(url).json()
        for park in response['data']:
            created_park = Park.objects.create(
                url = park['url'],
                full_name = park['fullName'],
                description = park['description'],
                latitude = park['latitude'],
                longitude = park['longitude'],
                state = park['states'],
                designation = park['designation'],
            )
            for image in park['images']:
                created_image = Image.objects.create(
                    park = created_park,  
                    credit = image['credit'],
                    title = image['title'],
                    alt_text = image['altText'],
                    caption = image['caption'],
                    url = image['url']
                )
            for address in park['addresses']:
                created_address = Address.objects.create(
                park = created_park,
                city = address['city'],
                state_code = address['stateCode']
                )
        return Response(None, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=False)
    def remove_historical_sites(self, request):
        Park.objects.filter(designation__icontains='historic').delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)