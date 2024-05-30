from django.contrib.auth.models import User
from django.db import models


class HydroponicsSystem(models.Model):
    owner = models.ForeignKey(User, related_name="systems", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name
