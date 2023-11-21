from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()
    movie_rate = models.FloatField()
    release_date = models.CharField(max_length=50)


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)


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
