from django.urls import path

from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="hostels"),
    path("<int:hostel_id>", views.hostel, name="hostel"),
    path("search", views.search, name="search"),
    path("hostelsEp/", include("api.urls")),
]
