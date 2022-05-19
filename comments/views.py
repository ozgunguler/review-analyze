from django.shortcuts import render
from reviewanalyze.generics import PostAPIView
from rest_framework import permissions
from comments.serializers import CommentCreateSerializer, CommentListSerializer
from reviewanalyze.constants import StandardResultsSetPagination, BaseResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from drf_excel.renderers import XLSXRenderer 
from drf_excel.mixins import XLSXFileMixin
import pandas as pd
from comments.models import Comments
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from comments.models import Comments


class CommentCreateAPIView(XLSXFileMixin, PostAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = CommentCreateSerializer
    parser_classes = MultiPartParser,
    renderer_classes = XLSXRenderer,

    @swagger_auto_schema(operation_summary="Read a new dataset from csv file, and save it to the mongodb")
    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_obj = request.data['csv_file']
        print("file obj: ", file_obj)
        if file_obj != '':
            data = pd.read_csv(file_obj)
            review_len = len(data['review'].values)
            for i in range(0, review_len):
                new_review = Comments()
                new_review.review = data['review'].values[i]
                new_review.sentiment = data['sentiment'].values[i]
                new_review.save()
            context = BaseResponse.success_response(200, "ok")
        else:
            context = BaseResponse.error_response(500, "Sorun var")
        return JsonResponse(data=context, status=200)


# class CommentListAPIView(ListAPIView):
#     permission_classes = permissions.AllowAny,
#     serializer_class = CommentListSerializer
#     pagination_class = StandardResultsSetPagination
#     queryset = Comments.objects.all()
#     lookup_field = '_id'


class CommentGetPositiveAPIView(ListAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = CommentListSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Comments.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(
            raise_exception=True
        )
        lst = Comments.objects.filter(sentiment="positive").count()
        print(lst)
        return Response(BaseResponse.success_response(200, "message"))