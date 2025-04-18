from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='genres')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True, default=2025)
    country = models.CharField(max_length=255, null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='authors', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст отзыва', null=True, blank=True)
    rating = models.FloatField(verbose_name="Оценка")
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    short_text = models.TextField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв на фильм {self.movie} - {self.rating}/10'