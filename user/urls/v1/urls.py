from django.conf.urls import url

from user.views.v1.views import UserLoginAPIView, UserRegistrationAPIView, UserLogoutAPIView

urlpatterns = [
    url(r'^login$', UserLoginAPIView.as_view(), name='user_login_api'),
    url(r'^register$', UserRegistrationAPIView.as_view(), name="user_register_api"),
    url(r'^logout$', UserLogoutAPIView.as_view(), name="user_logout_api"),
]
