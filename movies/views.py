from django.shortcuts import render

from movies.serializers import IMDBFileCreateSerializer, IMDBMoviesListSerializer
from reviewanalyze.generics import PostAPIView
from rest_framework import permissions
from reviewanalyze.constants import StandardResultsSetPagination, BaseResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from drf_excel.renderers import XLSXRenderer
from drf_excel.mixins import XLSXFileMixin
import pandas as pd
from movies.models import Movies
from django.http import JsonResponse
from rest_framework.generics import ListAPIView


class IMDBMovieCreateAPIView(XLSXFileMixin, PostAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = IMDBFileCreateSerializer
    parser_classes = MultiPartParser,
    renderer_classes = XLSXRenderer,

    @swagger_auto_schema(operation_summary="Read a new dataset from csv file, and save it to the mongodb (movies)")
    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_obj = request.data['csv_file']
        print("file obj: ", file_obj)
        data = []
        df = pd.read_csv(file_obj, index_col=None, sep='\t', low_memory=False)
        for i in range(0, len(df)):
            if df["region"].values[i] == "\\N":
                new_movie = Movies()
                new_movie.titleId = df['titleId'].values[i]
                new_movie.title = df['title'].values[i]
                new_movie.save()
        context = BaseResponse.success_response(200, "ok")
        return JsonResponse(data=context, status=200)


class IMDBMoviesListAPIView(ListAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = IMDBMoviesListSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Movies.objects.all()
    lookup_field = '_id'


# class CommentListAPIView(ListAPIView):
#     permission_classes = permissions.AllowAny,
#     serializer_class = CommentListSerializer
#     pagination_class = StandardResultsSetPagination
#     queryset = Comments.objects.all()
#     lookup_field = '_id'


# class CommentGetPositiveAPIView(ListAPIView):
#     permission_classes = permissions.AllowAny,
#     serializer_class = CommentListSerializer
#     pagination_class = StandardResultsSetPagination
#     queryset = Comments.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(
#             raise_exception=True
#         )
#         lst = Comments.objects.filter(sentiment="positive").count()
#         print(lst)
#         return Response(BaseResponse.success_response(200, "message"))