from rest_framework import serializers
from .models import Tovar

class TovarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tovar
		fields = "__all__"