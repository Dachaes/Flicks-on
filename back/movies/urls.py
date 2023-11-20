from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('movies/', views.movies),
    path('detail/<int:tmdb_pk>/', views.detail),
    path('detail/<int:movie_pk>/comment/', views.comment_create),
    path('detail/<int:movie_pk>/comment/<int:comment_pk>', views.comment_create),

]
