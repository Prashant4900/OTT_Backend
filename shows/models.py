from django.db import models
from smart_selects.db_fields import ChainedManyToManyField


# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=50, verbose_name='Platform Title')

    class Meta:
        verbose_name = 'Platforms'
        verbose_name_plural = 'Platform'

    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=50, verbose_name='Audio Title')

    class Meta:
        verbose_name = 'Languages'
        verbose_name_plural = 'Language'

    def __str__(self):
        return self.language


class Genres(models.Model):
    genres = models.CharField(max_length=50, verbose_name='Category Title')

    class Meta:
        verbose_name = 'Categorys'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.genres


class SubTitles(models.Model):
    subTitle = models.CharField(max_length=50, verbose_name='Sub Title')

    class Meta:
        verbose_name = 'SubTitles'
        verbose_name_plural = 'SubTitle'

    def __str__(self):
        return self.subTitle


class ShowsList(models.Model):
    ShowTitle = models.CharField(max_length=100, verbose_name='Title')
    ShowImage = models.URLField(verbose_name='Poster Image')
    ShowTrailer = models.URLField(blank=True, verbose_name='Trailer')
    Banner = models.BooleanField(default=False)
    Popular = models.BooleanField(default=False)
    Audio = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='Audio')
    Genre = models.ForeignKey(Genres, on_delete=models.CASCADE, related_name='Genre', verbose_name='Category')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='Platform')
    ShowDesc = models.TextField(verbose_name='Description')
    ShowReleaseDate = models.DateTimeField(verbose_name='Release Date')
    SubTitle = models.ForeignKey(
        SubTitles,
        on_delete=models.CASCADE,
        related_name='SubTitle',
        verbose_name='Sub Titles'
    )

    class Meta:
        verbose_name = 'Shows'
        verbose_name_plural = 'Show'

    def __str__(self):
        return self.ShowTitle


class SeasonsList(models.Model):
    SeasonTitle = models.CharField(max_length=15)
    SeasonDesc = models.TextField()
    SeasonImage = models.URLField()
    SeasonTrailer = models.URLField(blank=True)
    SeasonReleaseDate = models.DateTimeField()
    Series = models.ForeignKey(ShowsList, on_delete=models.CASCADE, related_name='Series')

    class Meta:
        verbose_name = 'Seasons'
        verbose_name_plural = 'Season'

    def __str__(self):
        return self.SeasonTitle


class EpisodeList(models.Model):
    EpisodeTitle = models.CharField(max_length=100)
    EpisodeDesc = models.TextField()
    EpisodeLink = models.URLField()
    EpisodeReleaseDate = models.DateTimeField()
    Show = models.ForeignKey(ShowsList, on_delete=models.CASCADE, related_name='Show', default='')
    Season = ChainedManyToManyField(
        SeasonsList,
        horizontal=True,
        related_name='Season',
        chained_field='Show',
        chained_model_field='Series'
    )

    class Meta:
        verbose_name = 'Episodes'
        verbose_name_plural = 'Episode'

    def __str__(self):
        return self.EpisodeTitle
