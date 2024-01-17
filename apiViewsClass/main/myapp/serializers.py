from rest_framework import serializers
from .models import *

class FilmsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Films
		fields = '__all__'

class AfishaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Afisha
		fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Director
		fields = '__all__'