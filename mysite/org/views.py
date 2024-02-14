from django.shortcuts import render
from rest_framework import viewsets, filters
# from rest_framework.views import APIView
from .models import Author, Book
from .serializer import AuthorSerializer, BookSerializer

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    List all workkers, or create a new worker.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['release_date']

