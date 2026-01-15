from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_todos, name="show_todos"),
]