from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
    
class Genres(models.Model):
    name = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()