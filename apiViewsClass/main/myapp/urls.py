from django.urls import path
from .views import *

urlpatterns = [
    path("films/", FilmsAV.as_view()),
    path("films/<int:pk>/", FilmAV.as_view()),
    path("afisha/", AfishasAV.as_view()),
    path("afisha/<int:pk>/", AfishaAV.as_view()),
    path("director/", DirectorsAV.as_view()),
    path("director/<int:pk>/", DirectorAV.as_view()),
    path("genre/", GenresAV.as_view()),
    path("genre/<int:pk>/", GenreAV.as_view()),
]