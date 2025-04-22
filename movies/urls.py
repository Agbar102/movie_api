from django.urls import path
from . import views

urlpatterns = [
    path('genre/', views.GenreAPIView.as_view(), name='genres'),
    path('movie/', views.MovieListAPIview.as_view(), name='movie'),
    path('movie-create/', views.MovieCreateAPIView.as_view(), name='movie_create'),
    path('movie-update/<int:pk>/', views.MovieUpdateAPIView.as_view(), name='movie_update'),
    path('review/', views.ReviewListAPIView.as_view(), name='reviews')
]