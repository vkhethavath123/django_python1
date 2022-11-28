from django.urls import path

from.views import json_body
urlpatterns = [
    path("", json_body, name="home"),
]