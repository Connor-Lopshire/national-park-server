from django.db import models
from django.contrib.auth.models import User

from nationalparkapi.models.parks import Park

class VisitedPark(models.Model):
    """data model for Visted Park join table"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visited_parks")
    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name="users_visited_parks")
    date = models.DateField()