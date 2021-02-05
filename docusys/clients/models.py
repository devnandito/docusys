"""Clients models."""

# Django
from django.db import models

# Utilities
from docusys.utils.models import CustomModel

class Client(CustomModel):
    """Client model."""

    first_name = models.CharField(max_length=140, blank=False, null=False)
    last_name = models.CharField(max_length=140, blank=False, null=False)
    ci = models.CharField(max_length=12, blank=False, null=False)
    birthday = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    nationality = models.CharField(max_length=140, blank=True, null=True)
    des_type = models.CharField(max_length=140, blank=True, null=True)
    code1 = models.CharField(max_length=20, blank=True, null=True)
    code2 = models.CharField(max_length=20, blank=True, null=True)
    code3 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direction = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    

    def __str__(self):
        return ('{} {}').format(self.first_name, self.last_name)