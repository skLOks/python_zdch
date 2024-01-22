from django.urls import path, include, re_path
from .views import *
import djoser

urlpatterns = [
    path("", Index.as_view()),
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path('log/', include('rest_framework.urls')),
    path('films/', FilmsAV.as_view()),
    path('films/<int:pk>/', FilmAV.as_view()),
    path('actors/', ActorsAV.as_view()),
    path('actors/<int:pk>/', ActorAV.as_view()),
    path('category/', CategorysAV.as_view()),
    path('category/<int:pk>/', CategoryAV.as_view()),
    path('rewiew/', RewiewsAV.as_view()),
    path('rewiew/<int:pk>/', RewiewAV.as_view()),
    path('genre/', GenresAV.as_view()),
    path('genre/<int:pk>/', GenreAV.as_view()),
    path('accounts/', Account_page.as_view()),
    path('accounts/profile/', account_profile_page),
]