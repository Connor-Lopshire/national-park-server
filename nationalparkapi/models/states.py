from django.db import models
class State(models.Model):
    """date model for park review"""
    state_code = models.CharField(max_length=2)