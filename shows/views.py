from django.shortcuts import render

from .models import Language, Genres, SubTitles, ShowsList, SeasonsList, EpisodeList
from .serializer import ShowsSerializer, SeasonsSerializer, EpisodeSerializer, LanguageSerializer, GenresSerializer, \
    SubTitlesSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView


# Create your views here.
def HomePage(request):
    return render(request, 'index.html')


class LanguageList(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class GenresList(generics.ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class SubTitlesList(generics.ListAPIView):
    queryset = SubTitles.objects.all()
    serializer_class = SubTitlesSerializer


class ShowsLists(APIView):
    def get(self, request):
        show = ShowsList.objects.all()
        serializer = ShowsSerializer(show, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SeasonList(APIView):
    def get(self, request):
        season = SeasonsList.objects.all()
        serializer = SeasonsSerializer(season, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EpisodeLists(generics.ListAPIView):
    queryset = EpisodeList.objects.all()
    serializer_class = EpisodeSerializer
