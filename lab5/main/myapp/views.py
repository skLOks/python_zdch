from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import Genre, Actor, Category, Film, Rewiew

class Index(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		return Response({
				'Ссылки на страницы для удобства': '',
		        'Начальная страница аутификации -': 'http://127.0.0.1:8000/auth/',
		        'Регистрация юзера -': 'http://127.0.0.1:8000/auth/users/',
		        'Аутификация -': 'http://127.0.0.1:8000/log/login/',
		        'Выход из аутификации -': 'http://127.0.0.1:8000/log/logout/',
			})

class FilmsAV(ListCreateAPIView):
	permission_classes = (AllowAny,)
	queryset = Film.objects.all()
	serializer_class = FilmSerializer

class FilmAV(RetrieveUpdateDestroyAPIView):
	permission_classes = (AllowAny,)
	queryset = Film.objects.all()
	serializer_class = FilmSerializer

class ActorsAV(ListCreateAPIView):
	permission_classes = (IsAdminUser,)
	queryset = Actor.objects.all()
	serializer_class = ActorSerializer

class ActorAV(RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAdminUser,)
	queryset = Actor.objects.all()
	serializer_class = ActorSerializer

class CategorysAV(ListCreateAPIView):
	permission_classes = (IsAdminUser,)
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryAV(RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAdminUser,)
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class RewiewsAV(ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = Rewiew.objects.all()
	serializer_class = RewiewSerializer

class RewiewAV(RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = Rewiew.objects.all()
	serializer_class = RewiewSerializer

class GenresAV(ListCreateAPIView):
	permission_classes = (IsAdminUser,)
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class GenreAV(RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAdminUser,)
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class Account_page(APIView):
	permission_classes = (AllowAny,)
	
	def get(self, request):
		return Response({
    		'Пусть будет эта страница': '',
    		})

@api_view(['GET'])
def account_profile_page(request, format=None):
    return Response({
        'Пусть будет эта страница': '',
        'Вернуть назад -': 'http://127.0.0.1:8000/',
    })