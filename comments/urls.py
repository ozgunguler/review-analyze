from django.conf.urls import url
from comments.views import CommentCreateAPIView, CommentListAPIView


urlpatterns = [
    url(r'^upload$', CommentCreateAPIView.as_view(), name='comment_create_api'),
    url(r'^list$', CommentListAPIView.as_view(), name='comment_list_api'),
]
