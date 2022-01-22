from django.urls import path

from . import views


urlpatterns = [
    path("", views.list_perks, name="list_perks"),
    path("badges", views.list_badges, name="list_badges"),
]
