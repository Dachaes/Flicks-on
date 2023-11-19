from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('detail/<int:movie_pk>/', views.detail),
    path('detail/<int:movie_pk>/comment/', views.comment_func),
]
