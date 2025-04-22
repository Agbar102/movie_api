from django.shortcuts import render
from rest_framework import generics

from movies.models import Genre, Movie, Review
from movies.serializers import GenreSerializer, MovieReadSerializer, MovieWriteSerializer, ReviewSerializer


class GenreAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieListAPIview(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReadSerializer


class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieWriteSerializer


class MovieUpdateAPIView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieWriteSerializer

class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

