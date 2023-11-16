from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    
    
class Genres(models.Model):
    name = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()