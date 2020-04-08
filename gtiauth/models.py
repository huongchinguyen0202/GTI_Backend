from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.FilePathField(path='avatar/', blank=True, null=True)
    phone = models.CharField(max_length=20)
    alternate_phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    street_address = models.CharField(max_length=200, blank=True, null=True)
    apartment_number = models.CharField(max_length=200, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)
