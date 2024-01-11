from django.shortcuts import render
from .models import Books
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BooksSerializer

# Create your views here.
class BooksView(ModelViewSet):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer

@api_view(['GET'])
def booksList(request):
	books = Books.objects.all()
	serializer = BooksSerializer(books, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def bookGet(request, pk):
	book = Books.objects.get(pk=pk)
	serializer = BooksSerializer(book)
	return Response(serializer.data)

@api_view(['DELETE'])
def bookDel(request, pk):
	books = Books.objects.get(pk=pk)
	books.delete()
	return Response("ваша книга громко плачет, удалили её значит...")

@api_view(['POST'])
def bookCreate(request):
	serializer = BooksSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def bookPut(request, pk):
	book = Books.objects.get(pk=pk)
	serializer = BooksSerializer(data=request.data, instance=book)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def bookPatch(request, pk):
	book = Books.objects.get(pk=pk)
	serializer = BooksSerializer(data=request.data, instance=book, partial=True)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)