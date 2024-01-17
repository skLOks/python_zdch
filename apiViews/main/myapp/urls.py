from django.urls import path, include
from .views import *
from rest_framework import routers

urlpatterns = [
    path("", TovarView.as_view({'get':'list', 'post': 'create'})),
    path("tovars/", tovarList),
    path("tovar/<int:pk>", tovarGet),
    path("tovardel/<int:pk>", tovarDel),
    path("tovaradd/", tovarCreate),
    path("tovarPut/<int:pk>", tovarPut),
    path("tovarPatch/<int:pk>", tovarPatch),
]
