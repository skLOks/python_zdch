from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *



# AV - Api Views

class FilmsAV(ListCreateAPIView):
	queryset = Films.objects.all()
	serializer_class = FilmsSerializer

class FilmAV(RetrieveUpdateDestroyAPIView):
	queryset = Films.objects.all()
	serializer_class = FilmsSerializer

class AfishasAV(ListCreateAPIView):
	queryset = Afisha.objects.all()
	serializer_class = AfishaSerializer

class AfishaAV(RetrieveUpdateDestroyAPIView):
	queryset = Afisha.objects.all()
	serializer_class = AfishaSerializer

class GenresAV(ListCreateAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class GenreAV(RetrieveUpdateDestroyAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class DirectorsAV(ListCreateAPIView):
	queryset = Director.objects.all()
	serializer_class = DirectorSerializer

class DirectorAV(RetrieveUpdateDestroyAPIView):
	queryset = Director.objects.all()
	serializer_class = DirectorSerializer
