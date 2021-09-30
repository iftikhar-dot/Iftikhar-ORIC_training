from django.urls import include, path
from . import views
from rest_framework import routers
from .views import *

urlpatterns = [
    path("hostels-all", views.HostelList.as_view()),
    path("hostels-all/<int:pk>", views.HostelDetail.as_view()),
    path("contacts-all", views.ContactList.as_view()),
    path("contacts-all/<int:pk>", views.ContactDetail.as_view()),
    path("owners-all", views.OwnerList.as_view()),
    path("owners-all/<int:pk>", views.OwnerDetail.as_view()),
    path("users-all", views.UserList.as_view()),
    path("users-all/<int:pk>", views.UserDetail.as_view()),
    path("utilities-all", views.UtilitiesList.as_view()),
    path("utilities-all/<int:pk>", views.UtilitiesDetail.as_view()),
]
