from re import T
from django.db import models
from datetime import datetime


GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
  

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    gender= models.CharField(choices=GENDER_CHOICES, max_length=128, null=True)
    age = models.IntegerField(null=True) 
    
    def __str__(self):
      return self.name
    
class Album(models.Model):
    musician = models.ForeignKey(Artist, related_name="album" , on_delete=models.CASCADE)
    album_name = models.CharField(max_length=255)
    release_date = models.DateField(default=datetime.today)
    rating_star = models.IntegerField()       
    
    def __str__(self):
        return self.album_name
    
class Song(models.Model):
    musician = models.ForeignKey(Artist, related_name="song", on_delete=models.CASCADE)
    song_title = models.CharField(max_length=400)
    song_url = models.URLField(("Song URL"), max_length=400, null=True)

    def __str__(self):
        return self.song_title