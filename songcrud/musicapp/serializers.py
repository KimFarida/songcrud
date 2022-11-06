#import modules
from .models import Artiste,Lyric,Song
from rest_framework import serializers


#Serializer for Songs
class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id','title','date_released','likes','artiste_id']

#Serializers for Artistes
class ArtisteSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True)

    class Meta:
        model = Artiste
        fields = ['id','first_name', 'last_name', 'age', 'song']
        
#Serializer for Lyric
class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['Content','song_id']