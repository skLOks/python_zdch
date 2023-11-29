from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request, name='siu', age=0):
	host = request.META['HTTP_HOST']
	user_agent = request.META['HTTP_USER_AGENT']
	path = request.path

	return HttpResponse(f'host{host} <br> browser: {user_agent} <br> Path: {path}' +
		f'<br> Имя: {name} <br> Возраст: {age}',
		headers={'jhbh':'jbihj'})