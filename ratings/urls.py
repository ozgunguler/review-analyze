from django.conf.urls import url
from ratings.views import IMDBRatingsCreateAPIView, IMDBRatingsListAPIView


urlpatterns = [
    url(r'^create$', IMDBRatingsCreateAPIView.as_view(), name='imdb_ratings_create_api'),
    url(r'^list$', IMDBRatingsListAPIView.as_view(), name='imdb_ratings_list_api'),
    # url(r'^deneme$', CommentGetPositiveAPIView.as_view(), name='clst_api'),
]
