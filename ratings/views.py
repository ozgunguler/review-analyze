from django.shortcuts import render
from rest_framework.generics import ListAPIView

from ratings.serializers import IMDBRatingsListSerializer
from movies.serializers import IMDBFileCreateSerializer
from reviewanalyze.generics import PostAPIView
from rest_framework import permissions
from reviewanalyze.constants import StandardResultsSetPagination, BaseResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from drf_excel.renderers import XLSXRenderer
from drf_excel.mixins import XLSXFileMixin
import pandas as pd
from ratings.models import Ratings
from django.http import JsonResponse


class IMDBRatingsCreateAPIView(XLSXFileMixin, PostAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = IMDBFileCreateSerializer
    parser_classes = MultiPartParser,
    renderer_classes = XLSXRenderer,

    @swagger_auto_schema(operation_summary="Read a new dataset from csv file, and save it to the mongodb (ratings)")
    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_obj = request.data['csv_file']
        print("file obj: ", file_obj)
        df = pd.read_csv(file_obj, index_col=None, sep='\t')
        for i in range(0, 1291):
            print(df['tconst'].values[i])
            new_rating = Ratings()
            new_rating.tconst = df['tconst'].values[i]
            new_rating.averageRating = df['averageRating'].values[i]
            new_rating.numVotes = df['numVotes'].values[i]
            new_rating.save()
        context = BaseResponse.success_response(200, "ok")
        return JsonResponse(data=context, status=200)


class IMDBRatingsListAPIView(ListAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = IMDBRatingsListSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Ratings.objects.all()
    lookup_field = '_id'


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