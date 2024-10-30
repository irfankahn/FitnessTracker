from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    goals = models.TextField(blank=True, null=True)

    class Meta:
        # Custom related names to avoid clashes
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
        # You can add custom permissions if needed
        permissions = [("can_view_custom_users", "Can view custom users")]
