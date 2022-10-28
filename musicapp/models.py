import imp
from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name, self.last_name

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()

    def __str__(self) -> str:
        return self.title

class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    song_id = models.IntegerField()

    def __str__(self) -> str:
        if len(self.content) > 50:
            return self.content
        else:
            return self.content[:50] + "..."

