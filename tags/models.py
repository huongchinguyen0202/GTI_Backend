from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)


class Tag(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)


