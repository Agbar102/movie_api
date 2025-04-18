from django.contrib import admin
from movies.models import *


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title',]

admin.site.register(Movie, MovieAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['rating','movie']

admin.site.register(Review, ReviewAdmin)
