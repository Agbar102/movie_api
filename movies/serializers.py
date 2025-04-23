from asyncio import start_server
from enum import unique

from django.utils.text import slugify
from rest_framework import serializers


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
        representation['title'] = f"{instance.title} ({instance.year})"
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

    def validate(self, data):
        user = self.context['request'].user
        movie = data.get('movie')

        if self.instance is None:
            if Review.objects.filter(author=user, movie=movie).exists():
                raise serializers.ValidationError("Вы уже оставили отзыв на этот фильм.")
        return data


class MovieStatsSerializer(serializers.ModelSerializer):
    reviews_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("title", "reviews_count", "average_rating")

    def get_reviews_count(self, obj):
        return obj.reviews.count()

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return round(sum(review.rating for review in reviews) / reviews.count(), 2)
        return None


class MovieSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Movie
        fields = ['title', 'slug', 'description']

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)
