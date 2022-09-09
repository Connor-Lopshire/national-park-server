from django.db import models
from nationalparkapi.models.parks import Park

class Image(models.Model):
    """data model for park images"""
    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name="images")
    credit = models.CharField()
    title = models.CharField()
    alt_text = models.CharField()
    caption = models.CharField()
    url = models.CharField()