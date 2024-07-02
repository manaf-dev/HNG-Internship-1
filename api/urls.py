from django.urls import path

from . import views


urlpatterns = [
    path("hello/", views.greetings, name="greetings"),
]
