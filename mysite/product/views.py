from django.shortcuts import render
from rest_framework import generics
from .models import Product, ProductStatus
from .serializer import ProductSerializer, ProductStatusSerilizer

# Create your views here.

class ProductViews(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductStatusView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductStatusSerilizer
