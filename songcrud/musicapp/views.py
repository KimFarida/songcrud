from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Artiste, Song, Lyric
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view

class ArtisteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    permission_classes = [permissions.IsAuthenticated]


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

class LyricViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET', 'POST', 'DELETE'])
def song_list(request):
    if request.method == 'GET':
        song = Song.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = song.filter(title__icontains=title)
        
        song_serializer = SongSerializer(song, many=True)
        return JsonResponse(song_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        song_data = JSONParser().parse(request)
        song_serializer = SongSerializer(data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse(song_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Song.objects.all().delete()
        return JsonResponse({'message': '{} Songs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    try: 
        song = Song.objects.get(pk=pk) 
    except Song.DoesNotExist: 
        return JsonResponse({'message': 'The song does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        song_serializer = SongSerializer(song) 
        return JsonResponse(song_serializer.data) 
 
    elif request.method == 'PUT': 
        song_data = JSONParser().parse(request) 
        song_serializer = SongSerializer(song, data=song_data) 
        if song_serializer.is_valid(): 
            song_serializer.save() 
            return JsonResponse(song_serializer.data) 
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        song.delete() 
        return JsonResponse({'message': 'Song was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    song = Song.objects.filter(published=True)
        
    if request.method == 'GET': 
        song_serializer = SongSerializer(song, many=True)
        return JsonResponse(song_serializer.data, safe=False)