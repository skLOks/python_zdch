from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def error(request):
	return HttpResponse("К сожалению произошла ошибка")
	