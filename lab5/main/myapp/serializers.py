from rest_framework import serializers
from .models import *

class FilmSerializer(serializers.ModelSerializer):
	class Meta:
		model = Film
		fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actor
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class RewiewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rewiew
		fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = '__all__'