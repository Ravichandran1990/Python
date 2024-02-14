from django.shortcuts import render
from rest_framework import generics
from .models import Song, Artist
from .serializer import ArtistSerializer, SongSerializer

# Create your views here.

class ArtistView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
