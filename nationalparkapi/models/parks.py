from django.db import models
from django.contrib.auth.models import User

class Park(models.Model):
    """data model for Park"""
    url = models.CharField(max_length=500)
    full_name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    bucket_list = models.ManyToManyField(User, related_name="bucket_list_parks")
    @property
    def visited(self):
        return self.__visited
    @visited.setter
    def visited(self, value):
        visit = value.visited_parks.all().filter(park_id=self.id)
        if len(visit) != 0 : 
            self.__visited = True
        else :
            self.__visited = False

            
    @property
    def in_bucket(self):
        return self.__in_bucket
    @in_bucket.setter
    def in_bucket(self, value):
        if self in value.bucket_list_parks.all():
            self.__in_bucket = True
        else : self.__in_bucket = False
