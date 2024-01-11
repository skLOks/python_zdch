from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostsView)

urlpatterns = router.urls

urlpatterns = [
    path("", PostsView.as_view({'get':'list', 'post': 'create'})),
    path("posts/", postsList),
    path("post/<int:pk>", postsGet),
    path("postdel/<int:pk>", postsDel),
    path("postadd/", postsCreate),
    path("postPut/<int:pk>", postsPut),
    path("postPatch/<int:pk>", postsPatch),
]