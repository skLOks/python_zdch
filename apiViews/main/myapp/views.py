from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TovarSerializer

# Create your views here.
class TovarView(ModelViewSet):
	queryset = Tovar.objects.all()
	serializer_class = TovarSerializer

@api_view(['GET'])
def tovarList(request):
	tovar = Tovar.objects.all()
	serializer = TovarSerializer(tovar, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def tovarGet(request, pk):
	tovar = Tovar.objects.get(pk=pk)
	serializer = TovarSerializer(tovar)
	return Response(serializer.data)

@api_view(['DELETE'])
def tovarDel(request, pk):
	tovar = Tovar.objects.get(pk=pk)
	tovar.delete()
	return Response("Товар не найден, мне кажется Дастан что-то промышляет...")

@api_view(['POST'])
def tovarCreate(request):
	serializer = TovarSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def tovarPut(request, pk):
	tovar = Tovar.objects.get(pk=pk)
	serializer = TovarSerializer(data=request.data, instance=tovar)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def tovarPatch(request, pk):
	tovar = Tovar.objects.get(pk=pk)
	serializer = TovarSerializer(data=request.data, instance=tovar, partial=True)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)