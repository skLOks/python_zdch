from django.shortcuts import render
from .models import Posts
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostsSerializer

# Create your views here.
class PostsView(ModelViewSet):
	queryset = Posts.objects.all()
	serializer_class = PostsSerializer

@api_view(['GET'])
def postsList(request):
	posts = Posts.objects.all()
	serializer = PostsSerializer(posts, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def postsGet(request, pk):
	posts = Posts.objects.get(pk=pk)
	serializer = PostsSerializer(posts)
	return Response(serializer.data)

@api_view(['DELETE'])
def postsDel(request, pk):
	posts = Posts.objects.get(pk=pk)
	posts.delete()
	return Response("всё смерть")

@api_view(['POST'])
def postsCreate(request):
	serializer = PostsSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def postsPut(request, pk):
	posts = Posts.objects.get(pk=pk)
	serializer = PostsSerializer(data=request.data, instance=posts)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def postsPatch(request, pk):
	posts = Posts.objects.get(pk=pk)
	serializer = PostsSerializer(data=request.data, instance=posts, partial=True)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)