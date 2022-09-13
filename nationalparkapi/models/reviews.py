from django.db import models

from nationalparkapi.models.parks import Park
from django.contrib.auth.models import User

class Review(models.Model):
    """date model for park review"""
    park= models.ForeignKey(Park, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    content = models.CharField(max_length=1000)