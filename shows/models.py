from django.db import models


# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language


class Genres(models.Model):
    genres = models.CharField(max_length=50)

    def __str__(self):
        return self.genres


class SubTitles(models.Model):
    subTitle = models.CharField(max_length=50)

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
    SubTitle = models.ForeignKey(SubTitles, on_delete=models.CASCADE, related_name='SubTitle',
                                 verbose_name='Sub Titles')
    ShowDesc = models.TextField(verbose_name='Description')
    ShowReleaseDate = models.DateTimeField(verbose_name='Release Date')

    class Meta:
        verbose_name = 'Show Lists'
        verbose_name_plural = 'Show List'

    def __str__(self):
        return self.ShowTitle


class SeasonsList(models.Model):
    SeasonTitle = models.CharField(max_length=15)
    SeasonDesc = models.TextField()
    SeasonImage = models.URLField()
    SeasonTrailer = models.URLField(blank=True)
    SeasonReleaseDate = models.DateTimeField()
    Series = models.ForeignKey(ShowsList, on_delete=models.CASCADE, related_name='Series')

    def __str__(self):
        return self.SeasonTitle


class EpisodeList(models.Model):
    EpisodeTitle = models.CharField(max_length=100)
    EpisodeDesc = models.TextField()
    EpisodeLink = models.URLField()
    EpisodeReleaseDate = models.DateTimeField()
    Show = models.ForeignKey(ShowsList, on_delete=models.CASCADE, related_name='Show', default='')
    Season = models.ManyToManyField(SeasonsList, related_name='Season', limit_choices_to={'Series': True})

    def __str__(self):
        return self.EpisodeTitle
