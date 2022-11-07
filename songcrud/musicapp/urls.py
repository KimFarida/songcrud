from django.urls import path
from .views import ArtisteListView,SongsListView,UrlOverview,SongDetailView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UrlOverview , name ='Urloverview'),
    path('art-api/', ArtisteListView , name ='art-api'),
    path('song-api/', SongsListView , name ='song-api'),
    path('song-detail/<int:pk>/', SongDetailView , name ='song-detail'),
]