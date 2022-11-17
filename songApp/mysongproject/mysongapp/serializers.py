from rest_framework import serializers
from .models import Album, Artist, Song



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('album', 'song_title', 'song_track', 'song_lyrics')


class AlbumSerializer(serializers.ModelSerializer):
    
    song = SongSerializer(read_only=True, many=True)
    
    class Meta:
        model  = Album
        fields = ('musician', 'album_name', 'release_date', 'record_label', 'rating_star', 'song') 


class ArtistSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True, many=True)
    class Meta:
        model  = Artist
        fields = ('name', 'gender', 'age', 'album')
        

