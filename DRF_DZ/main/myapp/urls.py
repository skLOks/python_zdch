from django.urls import path, include
from .views import *
from rest_framework import routers

urlpatterns = [
    path("", BooksView.as_view({'get':'list', 'post': 'create'})),
    path("books/", booksList),
    path("book/<int:pk>", bookGet),
    path("bookdel/<int:pk>", bookDel),
    path("bookadd/", bookCreate),
    path("bookPut/<int:pk>", bookPut),
    path("bookPatch/<int:pk>", bookPatch),
]