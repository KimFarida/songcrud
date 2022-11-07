#import modules
from .models import Artiste,Lyric,Song
from rest_framework import serializers


#Serializer for Songs
class SongSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Song
        fields = ['id','title','date_released','likes','artiste_id']

#Serializers for Artistes
class ArtisteSerializer(serializers.HyperlinkedModelSerializer):
    #song_rel = SongSerializer(many=True)

    class Meta:
        model = Artiste
        fields = ['id', 'first_name', 'last_name', 'age']
        
#Serializer for Lyric
class LyricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content','song_id']