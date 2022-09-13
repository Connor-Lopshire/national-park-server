from django.db import models
from nationalparkapi.models.parks import Park

class Image(models.Model):
    """data model for park images"""
    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name="images")
    credit = models.CharField(max_length=500, default="")
    title = models.CharField(max_length=500, default="")
    alt_text = models.CharField(max_length=500, default="")
    caption = models.CharField(max_length=500, default="")
    url = models.CharField(max_length=500, default="") 