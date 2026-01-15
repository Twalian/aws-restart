from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_comments, name="show_comments"),
]