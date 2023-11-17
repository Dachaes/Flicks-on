from django.shortcuts import render
from rest_framework.response import Response
from .models import Movie, Genre
from .utils import check_exist
from .serializers import MovieSerializer
import requests
import os

# Create your views here.
""" genre call function
def index(request):
    # 영화 더미데이터 가져오는 부분
    url = "https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=1"
    response = requests.get(
        url,
        headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.environ.get('API_TOKEN')}"
        }
    )
    data = response.json()
    for movie in data['results']:
        Movie.objects.create(
            title=movie["title"],
            poster_path=f'https://image.tmdb.org/t/p/original/{movie["poster_path"]}',
            tmdb_id=movie["id"],
        )
"""
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
    if not Genre.objects.exists():
        for genre in data['genres']:
            Genre.objects.create(
                name=genre["name"],
                tmdb_id=genre["id"],
            )
    # pass


def detail(request, movie_pk):
    movie = Movie.objects.filter(tmdb_id=movie_pk)
    if not movie:
        url = f"https://api.themoviedb.org/3/movie/{movie_pk}?language=ko-KR"
        response = requests.get(
            url,
            headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.environ.get('API_TOKEN')}"
            }
        )
        data = response.json()
        Movie.objects.create(
            title=data["title"],
            poster_path=f'https://image.tmdb.org/t/p/original/{data["poster_path"]}',
            tmdb_id=data["id"],
        )
