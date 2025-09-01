from django.db import models
from django.contrib.auth.models import User


class Equipment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='equipment')
    name = models.CharField(max_length=255)
    mac_address = models.CharField(max_length=17)
    ip_address = models.GenericIPAddressField()

    def __str__(self) -> str:
        return f"{self.name} ({self.mac_address})"
