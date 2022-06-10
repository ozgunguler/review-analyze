import pandas as pd
from django.db.models import Q
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from django.db.models import Max

from movies.models import Movies
from ratings.models import Ratings
from reviewanalyze.constants import BaseResponse

from reviewanalyze.serializers import MostAverageRatingMoviesSerializer


class DeleteEmptyIDDatasDestroyAPIView(DestroyAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = MostAverageRatingMoviesSerializer

    def delete(self, request, *args, **kwargs):
        ratings = Ratings.objects.filter(tconst="")
        ratings.delete()
        context = BaseResponse.success_response(status_code=200, message="OK")
        return JsonResponse(200, context)


class MostAverageRatingMoviesAPIView(RetrieveAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = MostAverageRatingMoviesSerializer
    queryset = Ratings.objects.all()

    def retrieve(self, request, *args, **kwargs):
        movies = Movies.objects.all()
        ordered_datas = []
        avg = Ratings.objects.all().order_by('-averageRating')
        for i in avg:
            for k in movies:
                if i.tconst == k.titleId:
                    ordered_datas.append({
                        "title": k.title,
                        "titleId": k.titleId,
                        "averageRating": i.averageRating,
                        "numVotes": i.numVotes
                    })
        data = ordered_datas[0:20]
        context = BaseResponse.json_response(200, data)
        # context = BaseResponse.success_response(200, "ok")
        return JsonResponse(data=context, status=200)
