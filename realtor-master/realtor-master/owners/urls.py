from django.urls import path

from django.urls import path, include

urlpatterns = [path("ownersEp/", include("api.urls"))]
