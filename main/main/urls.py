from django.contrib import admin
from django.urls import path
from multimain import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, kwargs={"interes1": "Программирование", "interes2": "Спорт"}, ),
    path("about/", views.about),
    path("contacts/", views.getcontacts),
]
