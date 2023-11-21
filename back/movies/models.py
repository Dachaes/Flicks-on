from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()
    movie_rate = models.FloatField()
    release_date = models.CharField(max_length=50)
    
    action = models.BooleanField(default=False)
    adventure = models.BooleanField(default=False)
    animation = models.BooleanField(default=False)
    comedy = models.BooleanField(default=False)
    crime = models.BooleanField(default=False)
    documentary = models.BooleanField(default=False)
    drama = models.BooleanField(default=False)
    family = models.BooleanField(default=False)
    fantasy = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    horror = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    mystery = models.BooleanField(default=False)
    romance = models.BooleanField(default=False)
    science_fiction = models.BooleanField(default=False)
    tv_movie = models.BooleanField(default=False)
    thriller = models.BooleanField(default=False)
    war = models.BooleanField(default=False)
    western = models.BooleanField(default=False)


class UserGenre(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    animation = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    crime = models.IntegerField(default=0)
    documentary = models.IntegerField(default=0)
    drama = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    history = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    mystery = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)
    science_fiction = models.IntegerField(default=0)
    tv_movie = models.IntegerField(default=0)
    thriller = models.IntegerField(default=0)
    war = models.IntegerField(default=0)
    western = models.IntegerField(default=0)


class Genre(models.Model):
    name = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/', blank=True)
