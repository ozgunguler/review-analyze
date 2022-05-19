from django.conf.urls import url
from comments.views import CommentCreateAPIView, CommentGetPositiveAPIView


urlpatterns = [
    url(r'^upload$', CommentCreateAPIView.as_view(), name='comment_create_api'),
    # url(r'^list$', CommentListAPIView.as_view(), name='comment_list_api'),
    url(r'^deneme$', CommentGetPositiveAPIView.as_view(), name='clst_api'),
]
