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