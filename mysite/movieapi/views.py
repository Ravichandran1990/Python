from django.shortcuts import render
from rest_framework import generics
from myapp.models import Movie
from .serializer import MovieSerializer
# Create your views here.

class MovieViews(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailsViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
