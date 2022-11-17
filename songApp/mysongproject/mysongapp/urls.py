from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArtistAPIView, ArtistDetailsApi, AlbumAPIView, AlbumDetailsAPi, SongAPIView, SongDetailsApi

urlpatterns = [
    path('artist_listings/', ArtistAPIView.as_view()),
    path('artist_details/<int:pk>', ArtistDetailsApi.as_view()),
    
    path('album_listings/', AlbumAPIView.as_view()),
    path('album_details/<int:pk>', AlbumDetailsAPi.as_view()),
    
    path('song_listings/', SongAPIView.as_view()),
    path('song_details/<int:pk>', SongDetailsApi.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)