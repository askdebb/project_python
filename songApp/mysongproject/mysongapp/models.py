from django.db import models






GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
  

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    gender= models.CharField(choices=GENDER_CHOICES, max_length=128, null=True)
    age = models.PositiveIntegerField(null=True) 
    
    def __str__(self):
      return self.name
    
    class Meta:
        verbose_name_plural = "Artist"
    
    
class Album(models.Model):
    musician = models.ForeignKey(Artist, related_name="album" , on_delete=models.CASCADE)
    album_name = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    record_label = models.CharField(max_length=255, null=True)
    rating_star = models.IntegerField()       
    
    def __str__(self):
        return self.album_name
    
    class Meta:
        verbose_name_plural = "Album"
    
class Song(models.Model):
    album = models.ForeignKey(Album, related_name="song", on_delete=models.CASCADE)
    song_title = models.CharField(max_length=400)
    song_track = models.PositiveIntegerField(null=True)
    song_lyrics = models.TextField(max_length=400, null=True)

    def __str__(self):
        return self.song_title
    
    class Meta:
        verbose_name_plural = "Song"
    