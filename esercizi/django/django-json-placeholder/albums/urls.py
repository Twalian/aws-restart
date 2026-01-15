from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_albums, name="show_albums"),
]