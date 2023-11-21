from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('movies/', views.movies),
    path('movies/recommend/<int:user_pk>/', views.recommend_movies),
    path('detail/<int:tmdb_pk>/', views.detail),
    path('detail/<int:movie_pk>/comment/', views.comment_cr),
    path('detail/<int:movie_pk>/comment/<int:comment_pk>', views.comment_ud),
    path('addimage/<int:user_pk>/', views.user_image),
    path('init/<int:user_pk>/', views.user_init),
]
