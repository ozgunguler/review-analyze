from django.conf.urls import url
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

router = routers.SimpleRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="Review - API Docs",
      default_version='v1',
      description="Review API Documentation - Swagger",
      terms_of_service="https://www.google.com/policies/terms/",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    url(r'^', include(router.urls)),
    url(r'^api-user/', include('rest_framework.urls', namespace='rest_framework')),

    path('v1/user/', include("user.urls.v1.urls")),
    path('v1/comment/', include("comments.urls")),


]
