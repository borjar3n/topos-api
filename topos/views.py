from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Topo
from .serializers import TopoSerializer

class TopoListCreate(generics.ListCreateAPIView):
    queryset = Topo.objects.all()
    serializer_class = TopoSerializer

class TopoRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topo.objects.all()
    serializer_class = TopoSerializer

