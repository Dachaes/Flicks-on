from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=256)
    
    
class Genres(models.Model):
    name = models.CharField(max_length=256)