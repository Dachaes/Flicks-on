from .models import Movie

def check_exist(tmdb_id):
    movie = Movie.objects.filter(tmdb_id=tmdb_id)
    if movie:
        return True
    else:
        return False