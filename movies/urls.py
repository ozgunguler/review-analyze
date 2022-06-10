from django.conf.urls import url
from movies.views import IMDBMovieCreateAPIView, IMDBMoviesListAPIView


urlpatterns = [
    url(r'^create$', IMDBMovieCreateAPIView.as_view(), name='imdb_movie_create_api'),
    url(r'^list$', IMDBMoviesListAPIView.as_view(), name='imdb_movies_list_api'),
    # url(r'^deneme$', CommentGetPositiveAPIView.as_view(), name='clst_api'),
]
