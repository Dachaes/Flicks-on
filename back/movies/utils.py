from .models import Movie
import requests



def check_exist(tmdb_id):
    movie = Movie.objects.filter(tmdb_id=tmdb_id)
    if movie:
        return 
    else:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?language=ko-KR"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMWYyMWQ4NmVkNTA5MTZmYTVkNzgxYWUzZjcyN2UzOSIsInN1YiI6IjY1NGQ5YWViMWFjMjkyN2IzMDJhNzFlMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6zjJFzvz_wLN9_I2XI6oo4JvxdcP-OESBRKTHPScC30"
        }
        