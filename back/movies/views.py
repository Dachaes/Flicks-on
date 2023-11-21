from re import L
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import is_valid_path
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre, Comment, UserImage, MovieGenre
from accounts.models import User
from .serializers import MovieSerializer, CommentSerializer, MovieDetailSerializer, ImageSerializer
import requests
import os


# Create your views here.
""" genre call function
def index(request):
    # 영화 더미데이터 가져오는 부분

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
    for page_num in range(1, 21):
        url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={page_num}"
        response = requests.get(
            url,
            headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.environ.get('API_TOKEN')}"
            }
        )
        data = response.json()
        for movie in data['results']:
            movie_obj = Movie.objects.create(
                title=movie["title"],
                poster_path=f'https://image.tmdb.org/t/p/original/{movie["poster_path"]}',
                tmdb_id=movie["id"],
                movie_rate = round(movie["vote_average"], 1),
                release_date=movie['release_date'],
            )
            genres = []
            for genre_num in movie['genre_ids']:
                if genre_num == 28: genres.append('action')
                elif genre_num == 12: genres.append('adventure')
                elif genre_num == 16: genres.append('animation')
                elif genre_num == 35: genres.append('comedy')
                elif genre_num == 80: genres.append('crime')
                elif genre_num == 99: genres.append('documentary')
                elif genre_num == 18: genres.append('drama')
                elif genre_num == 10751: genres.append('family')
                elif genre_num == 14: genres.append('fantasy')
                elif genre_num == 36: genres.append('history')
                elif genre_num == 27: genres.append('horror')
                elif genre_num == 10402: genres.append('music')
                elif genre_num == 9648: genres.append('mystery')
                elif genre_num == 10749: genres.append('romance')
                elif genre_num == 878: genres.append('science_fiction')
                elif genre_num == 10770: genres.append('tv_movie')
                elif genre_num == 53: genres.append('thriller')
                elif genre_num == 10752: genres.append('war')
                elif genre_num == 27: genres.append('western')
            
            for genre_name in genres:
                MovieGenre.objects.create(
                    movie=movie_obj,
                    genre=genre_name
                )
            
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
            movie_rate = round(data["vote_average"], 1),
            release_date=data['release_date'],
        )
    movie = get_object_or_404(Movie, tmdb_id=tmdb_pk)
    serializers = MovieDetailSerializer(movie)
    return Response(serializers.data)


@api_view(['GET', 'POST'])
def comment_cr(request, movie_pk):
    movie = get_object_or_404(Movie, tmdb_id=movie_pk)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response()

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        user = get_object_or_404(User, pk=request.data['pk'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['PUT', 'DELETE'])
def comment_ud(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT'])
def user_image(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    user_image = get_object_or_404(UserImage, user=user)
    if request.method == 'GET':
        serializer = ImageSerializer(user_image)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        serializer = ImageSerializer(user_image, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_init(request, user_pk):
    movies = get_list_or_404(Movie)
    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)