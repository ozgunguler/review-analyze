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


# class MostAverageRatingMoviesAPIView(ListAPIView):
#     permission_classes = permissions.AllowAny,
#     serializer_class = MostAverageRatingMoviesSerializer
#     queryset = Ratings.objects.all()
#
#     @swagger_auto_schema(operation_summary="Films that have most average ratings")
#     def list(self, request, *args, **kwargs):
#         max_rate_films = None
#         avg_arr = []
#         ratings = Ratings.objects.all()
#
#         for i in ratings:
#             avg_arr.append(i.averageRating)
#         max_rate = max(avg_arr)
#         for i in avg_arr:
#             max_rate_films = Ratings.objects.filter(averageRating=max_rate)
#         print(max_rate_films)
#         context = BaseResponse.json_response(200, data="ok")
#         return JsonResponse(200, context)


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
        # ratings = Ratings.objects.all()
        movies = Movies.objects.all()
        ordered_datas = []
        # Movies.objects.filter(titleId=ratings[i].tconst)
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
        print(data)
        # for i in range(0, 100):
        #     x = Movies.objects.filter(titleId=ratings[i].tconst)
        #     data.append({
        #         "titleId": x.titleId,
        #         "title": x.title,
        #         "averageRating": x.averageRating,
        #         "numVotes": x.numVotes,
        #         "language": x.language
        #     })
        # max_value = max(data['averageRating'])
        # df = pd.DataFrame(ratings)
        # print(df)
        # try:
        #     rating = Ratings.objects.get(tconst=tconst)
        # except:
        #     context = BaseResponse.error_response(404, message="Data could not be found by given tconst (id)")
        #     return JsonResponse(404, context)
        # movies = Movies.objects.filter(titleId=tconst)
        # print(movies)
        # for i in movies:
        #     data = {
        #         "titleId": i.titleId,
        #         "title": i.title,
        #         # "averageRating": rating.averageRating,
        #         # "numVotes": rating.numVotes,
        #         "language": i.language
        #     }
        context = BaseResponse.json_response(200, data)
        # context = BaseResponse.success_response(200, "ok")
        return JsonResponse(data=context, status=200)
