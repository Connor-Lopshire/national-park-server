from django.db import models
from django.contrib.auth.models import User

class Park(models.Model):
    """data model for Park"""
    url = models.CharField(max_length=150)
    full_name = models.CharField(max_length=100)
    description = models.CharField()
    latitude = models.CharField()
    longitude = models.CharField()
    state = models.CharField()
    designation = models.CharField()
    bucket_list = models.ManyToManyField(User, related_name="bucket_list_parks")