from django.conf.urls import url
from reviewanalyze.views import MostAverageRatingMoviesAPIView, DeleteEmptyIDDatasDestroyAPIView

urlpatterns = [
    # url(r'^list/(?P<tconst>[\w-]+)$', MostAverageRatingMoviesAPIView.as_view(), name='most_average_ratings_movies_api'),
    url(r'^list$', MostAverageRatingMoviesAPIView.as_view(), name='most_average_ratings_movies_api'),
    url(r'^destroy$', DeleteEmptyIDDatasDestroyAPIView.as_view(), name='delete_empty_id_datas_destroy_api'),
]
