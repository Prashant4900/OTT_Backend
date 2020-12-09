from rest_framework import serializers
from .models import ShowsList, SeasonsList, EpisodeList, Language, Genres, SubTitles


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('language',)


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('genres',)


class SubTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTitles
        fields = ('subTitle',)


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeList
        fields = ('EpisodeTitle', 'EpisodeDesc', 'EpisodeLink', 'EpisodeReleaseDate')


class SeasonsSerializer(serializers.ModelSerializer):
    episode = EpisodeSerializer(source='Season', many=True)

    class Meta:
        model = SeasonsList
        fields = ('SeasonTitle', 'SeasonDesc', 'SeasonImage', 'SeasonTrailer', 'SeasonReleaseDate', 'episode')


class ShowsSerializer(serializers.ModelSerializer):
    season = SeasonsSerializer(source='Series', many=True)
    Audio = LanguageSerializer()
    Genre = GenresSerializer()
    SubTitle = SubTitlesSerializer()

    class Meta:
        model = ShowsList
        fields = (
            'ShowTitle', 'ShowImage', 'ShowTrailer', 'Banner', 'Popular', 'Audio', 'Genre', 'SubTitle', 'ShowDesc',
            'ShowReleaseDate', 'season')
