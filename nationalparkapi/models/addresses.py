from operator import mod
from tkinter import Pack
from django.db import models

from nationalparkapi.models.parks import Park

class Address(models.Model):
    """data model for park address"""

    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name="addresses")
    city = models.CharField()
    state_code = models.CharField()