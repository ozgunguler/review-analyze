from rest_framework import filters, status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, CreateModelMixin


class PutAPIView(GenericAPIView, UpdateModelMixin):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostAPIView(GenericAPIView, CreateModelMixin):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
