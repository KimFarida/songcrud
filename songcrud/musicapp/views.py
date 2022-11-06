from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Artiste,Song
from .serializers import ArtisteSerializer, SongSerializer

#views handler
#url menu view
@api_view(['GET'])
def UrlOverview(request):
    api_urls = {
        'Artiste Lists': '/art-api/',
        'Songs Lists': '/song-api/',
        'Song Detail': '/song-detail/<int:id>',
        'Update Song': '/song-detail/<int:id>',
        'Delete Song': '/song-detail/<int:id>',
    }

    return Response(api_urls)


#Artistes list view handler
@api_view(['GET'])
def ArtisteListView(request):
    artiste = Artiste.objects.all()
    serializer = ArtisteSerializer(artiste, many = True)
    return Response(serializer.data)

#Songs list view handler
@api_view(['GET','POST'])
def SongsListView(request):
    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerializer(song, many = True)
        return Response(serializer.data)
    #code to post new songs to the list 
    if request.method == 'POST':
        data =request.data
        serializer = SongSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response("Invalid input", status= status.HTTP_400_BAD_REQUEST)


#Songs list view handler
@api_view(['GET','PUT','DELETE'])
def SongDetailView(request, pk):
    try:
        song = Song.objects.get(id=pk)
    except Song.DoesNotExist:
        return Response("Song does not exist", status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = SongSerializer(song, many = False)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = SongSerializer(song, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)

    if request.method == 'DELETE':
        song.delete()
        return Response({'message': 'song deleted'}, status= status.HTTP_204_NO_CONTENT)
        
        


