from django.contrib import admin
from .models import Artiste, Song, Lyric

# Register your models here.
@admin.site.register(Artiste)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'age')

@admin.site.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title','date_released', 'Artiste','artiste_id')

@admin.site.register(Lyric)
class LyricAdmin(admin.ModelAdmin):
    list_display = ('Content','Song','song_id')