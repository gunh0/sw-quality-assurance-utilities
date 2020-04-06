from django.shortcuts import render
from rest_framework import generics

from .models import RedPaser
from .serializers import RedPaserSerializer

class DataList(generics.ListCreateAPIView):
    queryset = RedPaser.objects.all()
    serializer_class = RedPaserSerializer

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RedPaser.objects.all()
    serializer_class = RedPaserSerializer
