from django.urls import path, include, re_path
from .views import *

urlpatterns = [
	path('user/<str:name>/<int:age>', index, name='home'),
	re_path(r'^user', index, name='home'),
	re_path(r'^', include('zadanie.urls')),
]