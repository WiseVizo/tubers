from . import views
from django.urls import path

urlpatterns = [
    path("", views.youtubers, name="youtubers"),
    path("<int:id>", views.youtuber_details, name="youtuber_detalis"),
    path("search", views.search, name="search"),
]