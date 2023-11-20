from urllib import response
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre, Comment
from accounts.models import User
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


@api_view(['GET'])
def movies(request):
    movies = get_list_or_404(Movie)[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, tmdb_pk):
    movie = Movie.objects.filter(tmdb_id=tmdb_pk)
    if not movie:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_pk}?language=ko-KR"
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(os.environ.get('API_TOKEN'))
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
        print(request.data)
        user = get_object_or_404(User, pk=request.data['pk'])
        # print(movie)
        # print(request.user)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        pass
    
    elif request.method == 'DELETE':
        pass
