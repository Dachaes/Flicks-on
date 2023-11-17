from django.shortcuts import render
from .models import Genres
import requests
import os

# Create your views here.
""" genre call function
def index(request):
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    response = requests.get(
        url,
        headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.environ.get('API_TOKEN')}"
        }
    )
    data = response.json()
    if not Genres.objects.exists():
        for genre in data['genres']:
            Genres.objects.create(
                name=genre["name"],
                tmdb_id=genre["id"],
            )
"""
def index(request):
    pass