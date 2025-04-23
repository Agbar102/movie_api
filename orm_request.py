#
# gen = Genre.objects.create(name="Фэнтези")
# mov = Movie.objects.create(title="Локи")
# mov.genres.set=([gen])
#
# user = User.objects.create(username="User10")
#
# mov1 = Movie.objects.get(title="Локи")
# user = User.objects.get(username="agbar")
# rew = Review.objects.create(movie=mov1, author=user, text="The best movie", rating=9)
#
#
#
#
# #1
# top_m = Movie.objects.annotate(res=Count("reviews")).order_by('-res')[:3]
#
# for el in top_m:
#     print(f"{el.title} - {el.res}")
#
#
#  #2
# avg_m = Movie.objects.annotate(res=Avg("reviews__rating"))
#
# for movie in avg_m:
#     print(f"{movie.title} - {movie.res}")
#
#
# #3
# movies = Movie.objects.filter(genre__name='Драма')
# for movie in movies:
#     print(el.title)
#
# #4
# rew = Review.objects.filter(author__username='user2').order_by('created_at')
#
# #5
# movies = Movie.objects.annotate(avg=Avg('reviews__rating')).filter(avg__gt=7)
#
# #6
# genres = Genre.objects.annotate(res=Count('genres'))
# for genre in genres:
#   print(genre.name, genre.res)
#
# #7
# country = Movie.objects.values_list('country', flat=True).distinct()
#
# #8
# movies = Movie.objects.annotate(res=Count('reviews')).filter(res=0)

