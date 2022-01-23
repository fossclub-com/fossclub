from django.urls import path

from . import views


urlpatterns = [
    path("", views.list_perks, name="list_perks"),
    path("badges/", views.list_badges, name="list_badges"),
    path("new/", views.PerkCreateView.as_view(), name="create_perk"),
    path("<int:perk_id>/", views.show_perk, name="show_perk")
]
