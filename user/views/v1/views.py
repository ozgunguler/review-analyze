from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework_jwt.settings import api_settings

from rest_framework.response import Response

from reviewanalyze.constants import BaseResponse
from user.serializers.v1.serializers import UserLoginSerializer, UserRegisterSerializer, UserLogoutSerializer

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginAPIView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(operation_summary="Login")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny, ]

    @swagger_auto_schema(operation_summary="Registration a new user")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = BaseResponse.success_response(message="User successfully created.", status_code=201)
        return Response(response)


class UserLogoutAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserLogoutSerializer

    @swagger_auto_schema(operation_summary="Logout api")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response.success_response(message="User successfully logged out.", status_code=201)
        return response
