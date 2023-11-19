from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre, Comment
from .utils import check_exist
from .serializers import MovieSerializer, CommentSerializer
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

    # 장르 가져오기
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
"""
def index(request):
    pass


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


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def comment_func(request, movie_pk):
    if request.method == 'POST':
        # movie = Movie.objects.get(pk=movie_pk)
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if request.user.is_authenticated and request.user.is_active:
                # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                serializer.save(user=request.user, movie=movie)
            else:
                # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        pass
    
    elif request.method == 'DELETE':
        pass
