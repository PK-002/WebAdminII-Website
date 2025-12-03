import datetime
from django.contrib import admin

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class Ranking(models.Model):
    list_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date created")
    image_url = models.URLField(blank=True,null=True)
    tier_config = models.JSONField(null=True)
    type = models.CharField(max_length=200, default="template")

class Image(models.Model):
    ranking = models.ForeignKey(Ranking, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='images/')
    
class Item(models.Model):
    Ranking = models.ForeignKey(Ranking, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    image_url = models.URLField(blank=True,null=True)
    tier_level = models.CharField(max_length=200)
    position = models.IntegerField(validators=[MinValueValidator(0)])

