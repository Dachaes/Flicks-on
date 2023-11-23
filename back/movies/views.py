from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre, Comment, UserImage, UserGenre
from accounts.models import User
from .serializers import GenreSerializer, MovieSerializer, CommentSerializer, MovieDetailSerializer, ImageSerializer, UserGenreSerializer
import requests
import os


def index(request):
    # 영화 더미데이터 가져오는 부분
    if not Movie.objects.exists():
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
                Movie.objects.create(
                    title=movie["title"],
                    poster_path=f'https://image.tmdb.org/t/p/original/{movie["poster_path"]}',
                    tmdb_id=movie["id"],
                    movie_rate = round(movie["vote_average"], 1),
                    release_date=movie['release_date'],
                    action= True if 28 in movie['genre_ids'] else False,
                    adventure = True if 12 in movie['genre_ids'] else False,
                    animation = True if 16 in movie['genre_ids'] else False,
                    comedy = True if 35 in movie['genre_ids'] else False,
                    crime = True if 80 in movie['genre_ids'] else False,
                    documentary = True if 99 in movie['genre_ids'] else False,
                    drama = True if 18 in movie['genre_ids'] else False,
                    family = True if 10751 in movie['genre_ids'] else False,
                    fantasy = True if 14 in movie['genre_ids'] else False,
                    history = True if 36 in movie['genre_ids'] else False,
                    horror = True if 27 in movie['genre_ids'] else False,
                    music = True if 10402 in movie['genre_ids'] else False,
                    mystery = True if 9648 in movie['genre_ids'] else False,
                    romance = True if 10749 in movie['genre_ids'] else False,
                    science_fiction = True if 878 in movie['genre_ids'] else False,
                    tv_movie = True if 10770 in movie['genre_ids'] else False,
                    thriller = True if 53 in movie['genre_ids'] else False,
                    war = True if 10752 in movie['genre_ids'] else False,
                    western = True if 27 in movie['genre_ids'] else False,
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
    print(data)
    if not Genre.objects.exists():
        for genre in data['genres']:
            Genre.objects.create(
                name=genre["name"],
                tmdb_id=genre["id"],
            )


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
            action= True if 28 in data['genre_ids'] else False,
            adventure = True if 12 in data['genre_ids'] else False,
            animation = True if 16 in data['genre_ids'] else False,
            comedy = True if 35 in data['genre_ids'] else False,
            crime = True if 80 in data['genre_ids'] else False,
            documentary = True if 99 in data['genre_ids'] else False,
            drama = True if 18 in data['genre_ids'] else False,
            family = True if 10751 in data['genre_ids'] else False,
            fantasy = True if 14 in data['genre_ids'] else False,
            history = True if 36 in data['genre_ids'] else False,
            horror = True if 27 in data['genre_ids'] else False,
            music = True if 10402 in data['genre_ids'] else False,
            mystery = True if 9648 in data['genre_ids'] else False,
            romance = True if 10749 in data['genre_ids'] else False,
            science_fiction = True if 878 in data['genre_ids'] else False,
            tv_movie = True if 10770 in data['genre_ids'] else False,
            thriller = True if 53 in data['genre_ids'] else False,
            war = True if 10752 in data['genre_ids'] else False,
            western = True if 27 in data['genre_ids'] else False,
        )
    movie = get_object_or_404(Movie, tmdb_id=tmdb_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment_cr(request, movie_pk):
    movie = get_object_or_404(Movie, tmdb_id=movie_pk)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

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
    genres = get_list_or_404(Genre)
    user = get_object_or_404(User, pk=user_pk)
    if request.method == 'GET':
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user_genre = UserGenre.objects.create(
            user = user,
            action = request.data['selectedGenres']['Action'],
            adventure = request.data['selectedGenres']['Adventure'],
            animation = request.data['selectedGenres']['Animation'],
            comedy = request.data['selectedGenres']['Comedy'],
            crime = request.data['selectedGenres']['Crime'],
            documentary = request.data['selectedGenres']['Documentary'],
            drama = request.data['selectedGenres']['Drama'],
            family = request.data['selectedGenres']['Family'],
            fantasy = request.data['selectedGenres']['Fantasy'],
            history = request.data['selectedGenres']['History'],
            horror = request.data['selectedGenres']['Horror'],
            music = request.data['selectedGenres']['Music'],
            mystery = request.data['selectedGenres']['Mystery'],
            romance = request.data['selectedGenres']['Romance'],
            science_fiction = request.data['selectedGenres']['Science Fiction'],
            tv_movie = request.data['selectedGenres']['TV Movie'],
            thriller = request.data['selectedGenres']['Thriller'],
            war = request.data['selectedGenres']['War'],
            western =  request.data['selectedGenres']['Western'],
        )
        serializer = UserGenreSerializer(user_genre)
        return Response(serializer.data)


@api_view(['POST'])
def recommend_movies(request, user_pk):
    id_score = []
    like_movie_list = []
    for item in request.data['user_genre'][0].items():
        if item[1] > 0:
            movies = Movie.objects.filter(**{item[0]: True})
            for movie in movies:
                if movie.tmdb_id:
                    score = item[1] * movie.movie_rate
                    id_score.append([movie.tmdb_id, score])
                    like_movie_list.append(movie)

    id_score.sort()
    res = [id_score.pop()]
    while id_score:
        tmp = id_score.pop()
        if tmp[0] == res[-1][0]:
            res[-1][1] += tmp[1]
        else:
            res.append(tmp)
    
    res.sort(key=lambda x: -x[1])

    movies = []
    for movie_info in res:
        for movie in like_movie_list:
            if movie_info[0] == movie.tmdb_id:
                movies.append(movie)
                break

    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)