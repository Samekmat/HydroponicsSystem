from django.contrib.auth.models import User
from django.db import models


class HydroponicsSystem(models.Model):
    owner = models.ForeignKey(
        User, related_name="systems", on_delete=models.CASCADE, help_text="Owner of the system."
    )
    name = models.CharField(max_length=64)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
