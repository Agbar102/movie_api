from django.contrib import admin
from movies.models import *


class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]

admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]

admin.site.register(Movie, MovieAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating','movie']

admin.site.register(Review, ReviewAdmin)
