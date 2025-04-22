from asyncio import start_server

from rest_framework import serializers

from orm_request import movie
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class MovieReadSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)
    genres = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Movie
        fields = ("genres", "title", "description", "year", "country", "average_rating", "slug", )


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.reviews.exists():
            review_serializer = ReviewSerializer(instance.reviews.all(), many=True)
            representation['reviews'] = review_serializer.data
        else:
            representation['reviews'] = []
        return representation



class MovieWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "description", "year", "genres", "country")



class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    created_at = serializers.DateTimeField(read_only=True)
    movie = serializers.CharField(source='movie.title')

    class Meta:
        model = Review
        fields = ("author", "rating", "short_text", "movie", "created_at")

    def validate_rating(self, value):
        if value < 1 or value > 10 :
            raise serializers.ValidationError("Рейтинг должен быть от 1 до 10")
        return value

