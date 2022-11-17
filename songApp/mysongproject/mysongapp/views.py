from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Album, Artist, Song
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer

# Create your views here.

class ArtistAPIView(APIView):
    
    def get(self, request, format=None):
        art = Artist.objects.all()
        serializer = ArtistSerializer(art, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    

class ArtistDetailsApi(APIView):
    
    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        art_id = self.get_object(pk)
        serializer = ArtistSerializer(art_id)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        art_put = self.get_object(pk)
        serializer = ArtistSerializer(art_put, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        art_id = self.get_object(pk)
        art_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class AlbumAPIView(APIView):
    
    def get(self, request, format=None):
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailsAPi(APIView):
    
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404
        
    
    def get(self, request, pk, format=None):
        album_id = self.get_object(pk)
        serializer = AlbumSerializer(album_id)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        album_put = self.get_object(pk)
        serializer = AlbumSerializer(album_put, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        alb_rm = self.get_object(pk)
        alb_rm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SongAPIView(APIView):
    
    def get(self, request):
        song_ID = Song.objects.all()
        serializer = SongSerializer(song_ID, many=True) 
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SongDetailsApi(APIView):
    
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        song_get = self.get_object(pk)
        serializer = SongSerializer(song_get)
        return Response(serializer.data)
    
    def put(self, request, pk):
        song_put = self.get_object(pk)
        serializer = SongSerializer(song_put, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        song_delete = self.get_object(pk)
        song_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
