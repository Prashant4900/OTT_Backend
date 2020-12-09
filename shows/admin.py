from django.contrib import admin
from .models import Platform, Language, Genres, SubTitles, ShowsList, SeasonsList, EpisodeList
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter


# Register your models here.
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language')
    list_display_links = ('id', 'language')


class SubTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'subTitle')
    list_display_links = ('id', 'subTitle')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'genres')
    list_display_links = ('id', 'genres')


class ShowsAdmin(admin.ModelAdmin):
    list_display = ('ShowTitle', 'ShowDesc', 'ShowReleaseDate')
    list_display_links = ('ShowTitle',)
    list_filter = (
        'ShowReleaseDate',
        'Banner',
        'Popular',
        ('Audio', RelatedDropdownFilter),
        ('Genre', RelatedDropdownFilter),
        ('platform', RelatedDropdownFilter),
        ('SubTitle', RelatedDropdownFilter),
    )
    search_fields = ('ShowTitle', 'ShowDesc', 'ShowReleaseDate')
    fieldsets = (
        ("Main Details", {
            'fields': ('ShowTitle', 'ShowTrailer', "ShowImage", 'ShowDesc', 'Genre', 'ShowReleaseDate',)
        }),
        ('Side Details', {
            'classes': ('collapse',),
            'fields': ('Banner', 'Popular', 'Audio', 'platform', 'SubTitle'),
        }),
    )


class SeasonListAdmin(admin.ModelAdmin):
    list_display = ('id', 'SeasonTitle', 'Series')
    list_display_links = ('id', 'SeasonTitle')
    list_filter = (
        'SeasonReleaseDate',
        ('Series', RelatedDropdownFilter),
    )
    search_fields = ('SeasonTitle', 'Series', 'SeasonReleaseDate')


class EpisodeListAdmin(admin.ModelAdmin):
    filter_horizontal = ('Season',)
    list_display = ('id', 'EpisodeTitle')
    list_display_links = ('id', 'EpisodeTitle')
    list_filter = (
        'EpisodeReleaseDate',
        ('Show', RelatedDropdownFilter),
    )
    search_fields = ('EpisodeTitle', 'EpisodeReleaseDate', 'EpisodeDesc', 'EpisodeLink')


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Genres, GenreAdmin)
admin.site.register(SubTitles, SubTitleAdmin)
admin.site.register(ShowsList, ShowsAdmin)
admin.site.register(SeasonsList, SeasonListAdmin)
admin.site.register(EpisodeList, EpisodeListAdmin)
