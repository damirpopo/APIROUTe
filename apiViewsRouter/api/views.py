from django.shortcuts import render
from .models import Pet,Zakaz
from .serializers import Petserializer,Zakazserializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView


class PetView(ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = Petserializer

class Pet2View(RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = Petserializer

class ZakazView(ListAPIView):
    queryset = Zakaz.objects.all()
    serializer_class = Zakazserializer

class Zakaz2View(RetrieveUpdateDestroyAPIView):
    queryset = Zakaz.objects.all()
    serializer_class = Zakazserializer


